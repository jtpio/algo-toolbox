from prime_sieve import sieve
from is_prime import is_prime

s, ps = sieve(1000000)

assert is_prime(31, s, ps) == True
assert is_prime(97, s, ps) == True
assert is_prime(100000000, s, ps) == False
assert is_prime(999983, s, ps) == True
