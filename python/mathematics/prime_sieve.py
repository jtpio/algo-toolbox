def sieve(n):
    """ Generate the list of primes below n
    Parameters
    ----------
    n: int
        Limit
    """
    ps = []
    a = [False] * 2 + [True] * n
    for i in range(2, int(n+1)):
        if a[i]:
            for j in range(i*i, n+1, i):
                a[j] = False
            ps.append(i)
    return (a, ps)
