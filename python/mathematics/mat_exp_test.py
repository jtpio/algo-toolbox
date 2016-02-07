import numpy as np
from mat_exp import mat_exp


def compute_ans(n):
    res = mat_exp(m, n, MOD) * m0
    xn = (2 * res.item(0, 0)) % MOD - 1
    return xn

# Tests taken from Google Code Jam 2008, Round 1A, Problem C, Numbers
m = np.matrix([[3, 5], [1, 3]])
m0 = np.matrix([[1], [0]])
MOD = 1000

tests = [
    [1605814285, 735],
    [1999999991, 543],
    [2000000000, 751]
]

for test in tests:
    assert compute_ans(test[0]) == test[1]
