import string

A = ''.join(str(x) for x in range(10)) + string.ascii_lowercase


def dec_to_base(n, b):
    """
    Convert an integer n in base 10 to its corresponding string in base b
    Parameters
    ----------
    n: int
        The input integer
    b: int
        Base. 2 <= b <= 36

    Returns
    -------
    out: str
        The string representation of n in base b
    """
    if not 2 <= b <= 36:
        raise ValueError('base b must be between 2 and 36')
    ans = ''
    while n > 0:
        r = n % b
        n //= b
        ans = A[r] + ans
    return ans
