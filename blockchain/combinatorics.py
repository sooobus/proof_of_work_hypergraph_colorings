import operator as op
from functools import reduce
import numpy as np

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer // denom

def index2combination(n, k, m):
    ans = np.array([])
    nxt = 1
    while k > 0:
        if m < ncr(n - 1, k - 1):
            ans = np.append(ans, nxt)
            k -= 1
        else:
            m -= ncr(n - 1, k - 1)
        n -= 1
        nxt += 1
    return ans

def set_family_from_number(n, k, s, m):
    numbers = index2combination(ncr(n, k), s, m)
    print(numbers)
    sets = [index2combination(n, k, i) for i in numbers]
    return sets
