from prime_sieve import sieve
from prime_factors import prime_factors

s, ps = sieve(1000000)
assert prime_factors(30, ps) == [2, 3, 5]
assert prime_factors(123456789, ps) == [3, 3, 3607, 3803]

# 999983 is prime
assert prime_factors(999983, ps) == [999983]
