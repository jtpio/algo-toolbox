from decimal_to_base import dec_to_base

assert dec_to_base(2, 2) == '10'
assert dec_to_base(3, 2) == '11'
assert dec_to_base(82, 3) == '10001'
assert dec_to_base(1337, 10) == '1337'
assert dec_to_base(1293123867, 36) == 'ldw4rf'

try:
    res = dec_to_base(82, 37)
except ValueError as e:
    assert str(e) == 'base b must be between 2 and 36'
