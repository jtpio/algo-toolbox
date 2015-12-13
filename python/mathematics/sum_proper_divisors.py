def sum_proper_divisors(n):
    res = 1
    square_root = int(n ** 0.5)

    if square_root ** 2 == n:
        res += square_root

    for i in range(2, square_root):
        if n % i == 0:
            res += i + n // i

    return res
