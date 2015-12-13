from cycle_finding import floyd, brent


def bit_switch(x):
    return 1 - x


def mod(x):
    return (x + 1) % 5 + 1


def uva_gen(Z, I, M):
    def f(x):
        return (Z * x + I) % M
    return f

assert floyd(bit_switch, 0) == (0, 2)
assert brent(bit_switch, 0) == (0, 2)
assert floyd(mod, 4) == (0, 5)
assert brent(mod, 4) == (0, 5)

# Uva 350 sample test cases
uva = [
    7, 5, 12, 4,
    5173, 3849, 3279, 1511,
    9111, 5309, 6000, 1234,
    1079, 2136, 9999, 1237
]
uva_ans = [6, 546, 500, 220]
T = len(uva) // 4
for i in range(0, T, 4):
    Z, I, M, L = uva[i:i+4]
    f = uva_gen(Z, I, M)
    assert floyd(f, L)[1] == uva_ans[i // 4]
    assert brent(f, L)[1] == uva_ans[i // 4]
