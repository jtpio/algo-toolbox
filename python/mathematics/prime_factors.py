def prime_factors(n, ps=[]):
    """ Return the list of prime factors of n
    Parameters
    ----------
    n: int
    ps: list
        List of prime factors to use
    """
    if len(ps) == 0:
        return []
    fs = []
    i = 0
    pf = ps[i]
    while pf * pf <= n:
        while n % pf == 0:
            n //= pf
            fs.append(pf)
        i += 1
        pf = ps[i]
    if n != 1:
        fs.append(n)
    return fs
