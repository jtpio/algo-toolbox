class SegmentTree:
    """ SegmentTree Tree implementation to provide fast Range Min Queries """
    def __init__(self, a):
        self.a = a
        self.n = len(self.a)
        self.st = [0] * self.n * 4
        self._build(1, 0, self.n - 1)

    def _build(self, p, L, R):
        if L == R:
            self.st[p] = L
        else:
            p1 = self._build(self._left(p), L, (L + R) // 2)
            p2 = self._build(self._right(p), (L + R) // 2 + 1, R)
            self.st[p] = p1 if self.a[p1] <= self.a[p2] else p2

        return self.st[p]

    def _left(self, p):
        return p << 1

    def _right(self, p):
        return (p << 1) + 1

    def _rmq(self, p, L, R, i, j):
        if i > R or j < L:
            return -1
        if L >= i and R <= j:
            return self.st[p]

        p1 = self._rmq(self._left(p), L, (L + R) // 2, i, j)
        p2 = self._rmq(self._right(p), (L + R) // 2 + 1, R, i, j)

        if p1 == -1 or p2 == -1:
            return max(p1, p2)

        return p1 if self.a[p1] <= self.a[p2] else p2

    def _update(self, p, L, R, i, value):
        if not L <= i <= R:
            return self.st[p]
        if L == i == R:
            self.a[i] = value
            self.st[p] = L
            return L
        p1 = self._update(self._left(p), L, (L + R) // 2, i, value)
        p2 = self._update(self._right(p), (L + R) // 2 + 1, R, i, value)
        self.st[p] = p1 if self.a[p1] <= self.a[p2] else p2
        return self.st[p]

    def rmq(self, i, j):
        return self._rmq(1, 0, self.n - 1, i, j)

    def update(self, i, value):
        return self._update(1, 0, self.n - 1, i, value)
