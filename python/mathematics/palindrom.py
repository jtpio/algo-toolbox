def is_palindrom(c):
    """ Return True if the string <c> is a palindrom """
    c = str(c)
    for i, e in enumerate(c):
        if i > len(c)/2:
            break
        else:
            if e != c[len(c)-i-1]:
                return False
    return True
