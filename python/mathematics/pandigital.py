import string


def is_pandigital(n, b=10, zeroless=False, unique=False):
    """ Return True if the number n is pandigital in base b.
    Parameters
    ----------
    n: int or string
        The number to test.
    b: int
        The base to choose, defaults is 10.
    zeroless: bool
        Zero is a forbidden digit, default is False
    unique: bool
        Digits must appear only once, default is False

    Returns
    -------
    out: bool
        True if n is pandigital in respect of the given parameters,
        False otherwise
    """
    offset = 1 if zeroless else 0
    alphabet = (string.digits + string.ascii_letters)[offset:b]
    ns = str(n)
    if unique:
        return len(ns) == len(alphabet) and ns <= (alphabet[-1] * len(ns))
    if len(ns) < b - offset:
        return False
    s = set(ns)
    sa = set(alphabet)
    return s.issubset(sa)
