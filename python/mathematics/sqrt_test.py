import operator
import math
from functools import reduce
from sqrt import sqrt_int


def prod(xs):
    return reduce(operator.mul, xs, 1)

assert sqrt_int(4) == 2
assert sqrt_int(100) == 10


# The following example taken from the MathsJam 2015/11 puzzle
ls = list(range(1, 50)) + list(range(51, 101))
fls = [math.factorial(x) for x in ls]
big_number = prod(fls)

N = 100
A = 1
for i in range(2, N, 2):
    p = (N - i) // 2
    A *= (i ** p)
    A *= ((i + 1) ** p)

expected_square_root = A * (2 ** 25)

assert sqrt_int(big_number) == expected_square_root
