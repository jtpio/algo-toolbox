def mat_exp(mat, p, mod):
    """
    Fast Matrix Exponentiation with modulo
    Parameters
    ----------
    mat: numpy matrix
        The matrix to exponentiate. It must be a matrix that supports the *
        operator.
    p: int
        The power to raise the matrix to.
    mod: int
        The modulo value used to calculate elements of the matrix

    Returns
    -------
    out: numpy matrix
        Exponentiated matrix
    """
    if p < 0:
        mat = mat ** (-1)
        p = -p
    if p == 0:
        return mat
    mat2 = 1
    while p > 1:
        if p % 2 == 0:
            mat = (mat * mat) % mod
            p //= 2
        else:
            mat2 = (mat2 * mat) % mod
            mat = (mat * mat) % mod
            p = (p - 1) // 2
    return (mat * mat2) % mod
