import numpy as np
import itertools as it
import time

def greedy_set_size(M):
    rest = M
    assert 0 not in np.sum(rest, axis=0)
    chosen = np.zeros(M.shape[1]).astype(int)
    counter = 0
    while 0 in chosen:
        rest -= chosen
        rest = rest.clip(min=0)
        chosen_ind = np.argmax(np.sum(rest, axis=1))
        chosen |= rest[chosen_ind, :]
        rest = np.delete(rest, chosen_ind, 0)
        counter += 1
    return counter

def generate_test_matrix(n, k, s):
    M = np.hstack((np.zeros((s, n - k)), np.ones((s, k)))).astype(int)
    for i in range(M.shape[0]):
        np.random.shuffle(M[i,:])
    if 0 in np.sum(M, axis=0):
        return np.zeros(1)
    return M
 
def test(s, n, k, M):
    counter = 0
    greedy_size = greedy_set_size(M)
    for k in range(2, greedy_size):
        c_s_k = it.combinations(range(s), k)
        for comb in c_s_k:
            chosen = M[comb, :]
            if 0 not in np.sum(chosen, axis=0):
                return (0, k)
                #print(chosen)
                return
    return (1, greedy_set_size(M))

def measure_time(n, k, s):
    sum_t = 0
    bad_generated_mx = 0
    only_greedy = 0
    success = 0
    for i in range(10):
        mx = generate_test_matrix(n, k, s)
        if not mx.any():
            bad_generated_mx += 1
        else:
            start = time.time()
            res = test(s, n, k, mx)
            if res[0] == 1:
                only_greedy += 1
            else:
                end = time.time()
                sum_t += end - start
                success += 1
                sum_t += end - start
    if success == 0: 
        success = 1
    return (n, k, s, only_greedy, bad_generated_mx, round(sum_t / success, 3))

print("n k s жадно плохо ср.успех")
for n in [10, 20, 50, 100, 300, 500]:
    for k in [n // 2, n // 3, n // 4, n // 5, n // 10]:
        for s in [10, 20, 50, 100]:
            print(" ".join(map(str, measure_time(n, k, s))))
