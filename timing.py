import numpy as np
import itertools as it
import time

def test(s=50, n=500):
    M = np.random.choice(2, size=(s, n)) 
    counter = 0
    for k in range(2, s):
        c_s_k = it.combinations(range(s), k)
        for comb in c_s_k:
            chosen = M[comb, :]
            if 0 not in np.sum(chosen, axis=0):
                print(k)
                #print(chosen)
                return

sum_t = 0
for i in range(10):
    start = time.time()
    test()
    end = time.time()
    sum_t += end - start
    print(end - start)
print("Mean run time:", sum_t / 10)
