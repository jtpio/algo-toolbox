class UnionFind:
    """ Union Find implementation with path compression """
    def __init__(self, n):
        self.n = n
        self.nsets = n
        self.p = list(range(n))
        self.size = [1] * n
        self.rank = [0] * n

    def connected(self, u, v):
        return (u == v) or (self.find(u) == self.find(v))

    def find(self, u):
        v = u
        while v != self.p[v]:
            self.p[v] = self.p[self.p[v]]
            v = self.p[v]
        return v

    def union(self, u, v):
        x, y = self.find(u), self.find(v)
        if x == y:
            return
        self.nsets -= 1
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
            self.size[x] += self.size[y]
        else:
            self.p[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def set_size(self, u):
        return self.size[self.find(u)]
