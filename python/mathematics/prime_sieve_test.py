from prime_sieve import sieve

first_10_primes = [2, 3, 5, 7, 11]
primes = sieve(11)[1]

assert primes == first_10_primes

lookup, ls = sieve(1000000)

# Verify that some numbers are primes or not
assert lookup[5] == True
assert lookup[31] == True
assert lookup[999983] == True
assert lookup[999987] == False
