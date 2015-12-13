def is_prime(n, s=[], ps=[]):
    """ Check whether a reasonably small number is prime or not.
        The user has the responsability to provide a big enough list of primes.
        The function will return True if it can't find a prime that divides n.
    Parameters
    ----------
    n: int
        Number to check
    s: list
        pre-calculated sieve to use
    ps: list
        list of primes to use for divisibility checks
    """
    if n < len(s) and len(s) > 0:
        return s[n]
    for p in ps:
        if n % p == 0:
            return False
    return True
