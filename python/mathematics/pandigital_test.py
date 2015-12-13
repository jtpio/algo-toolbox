from pandigital import is_pandigital

assert is_pandigital(1) == False
assert is_pandigital(1, 2) == False
assert is_pandigital('10', 2) == True
assert is_pandigital('10', 2, True) == False
assert is_pandigital('110', 2, unique=True) == False

assert is_pandigital(1234567890) == True
assert is_pandigital(1234567890, zeroless=True) == False

assert is_pandigital(123, b=4, zeroless=True) == True
assert is_pandigital('021', b=3) == True
assert is_pandigital('021', b=3, unique=True) == True
