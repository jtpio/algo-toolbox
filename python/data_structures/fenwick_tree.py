class FenwickTree:
    """
    Fenwick Tree implementation to provide fast Range Sum Queries
    """
    def __init__(self, n):
        self.ft = [0] * (n + 1)

    def ls_one(self, k):
        return k & (-k)

    def rsq_one(self, b):
        s = 0
        while b > 0:
            s += self.ft[b]
            b -= self.ls_one(b)
        return s

    def rsq(self, a, b):
        return self.rsq_one(b) - (0 if a == 1 else self.rsq_one(a - 1))

    def adjust(self, k, v):
        while k < len(self.ft):
            self.ft[k] += v
            k += self.ls_one(k)
