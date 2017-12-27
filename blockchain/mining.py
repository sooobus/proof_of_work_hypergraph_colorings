import numpy as np
import itertools as it
import time
import random
import combinatorics

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

def generate_test_matrix(n, k, s, number):
    sets = set_family_from_number(n, k, s, number)
    M = np.zeros((s, n)) 
    for i in range(M.shape[0]):
        M[i, sets[i]] += 1
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

def mine_process(n, k, s, key_hash, set_size):
    #seed = key_hash
    mx = generate_test_matrix(n, k, s, random.randrange(set_size))    
    while not mx.any():
        key_hash += 1
        #seed = prev_hash
        mx = generate_test_matrix(n, k, s, random.randrange(set_size))
    res = test(s, n, k, mx)
    if res[0] == 1:
        res = mine_process(n, k, s, key_hash + 1, set_size)
    return res, key_hash

def mine(n, k, s, prev_hash):
    set_size = ncr(ncr(n, k), s)
    res = mine_process(n, k, s, prev_hash, set_size)

