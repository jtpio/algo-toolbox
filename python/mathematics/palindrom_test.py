from palindrom import is_palindrom

assert is_palindrom('abcd') == False
assert is_palindrom('aaabaaa') == True
assert is_palindrom('') == True

# Can also be used for numbers
assert is_palindrom(12345654321) == True
