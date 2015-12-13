def dec_to_bin_slow(n):
    """ Manually transform a decimal number to its binary representation.
    Parameters
    ----------
    n: int
        Number in base 10
    """
    res = ''
    if n < 0:
        raise ValueError
    if n == 0:
        return '0'
    while n > 0:
        res = str(n % 2) + res
        n = n >> 1
    return res


def dec_to_bin(n):
    """ Return the binary representation of the number n expressed in base 10
    Parameters
    ----------
    n: int
        Number in base 10
    """
    return bin(n)[2:]
