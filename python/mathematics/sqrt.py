def sqrt_int(n):
    """ Calculate the integer square root of n, defined as the largest integer
    r such that r*r <= n
    Borrowed from: https://gist.github.com/hampus/d2a2d27f37415d37f7de

    Parameters
    ----------
    n: int
        The integer to calculate the square root from

    Returns
    -------
    out: int
        The value of the square root
    """
    r = 1
    while r * r <= n:
        r <<= 1
    b = r = r >> 1
    while b > 1:
        b >>= 1
        r2 = r + b
        if r2 * r2 <= n:
            r = r2
    return r
