def floyd(f, start):
    """ Floyd Cycle Finding implementation
    Parameters
    ----------
    f: function
        The function to transform one value to its successor
    start:
        The start point from where the cycle detection starts.

    Returns
    -------
    out: tuple:
    - mu: int
        Position at which the cycle starts
    - length: int
        The length of the cycle
    """
    slow, fast = f(start), f(f(start))
    while slow != fast:
        slow, fast = f(slow), f(f(fast))
    mu = 0
    fast = start
    while slow != fast:
        slow, fast = f(slow), f(fast)
        mu += 1
    length = 1
    fast = f(slow)
    while slow != fast:
        fast = f(fast)
        length += 1
    return (mu, length)


def brent(f, start):
    p = length = 1
    slow, fast = start, f(start)
    while slow != fast:
        if p == length:
            slow = fast
            p *= 2
            length = 0
        fast = f(fast)
        length += 1
    mu = 0
    slow = fast = start
    for i in range(length):
        fast = f(fast)
    while slow != fast:
        slow, fast = f(slow), f(fast)
        mu += 1
    return mu, length
