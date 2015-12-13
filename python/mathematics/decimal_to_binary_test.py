from decimal_to_binary import dec_to_bin, dec_to_bin_slow

assert dec_to_bin(42) == '101010'

# The 2 different functions must return the same result
NUMBERS_TO_TEST = 100000
for i in range(NUMBERS_TO_TEST):
    assert dec_to_bin(i) == dec_to_bin_slow(i)
