from union_find import UnionFind

uf = UnionFind(5)

assert uf.nsets == 5

uf.union(0, 1)

assert uf.nsets == 4

uf.union(2, 3)

assert uf.nsets == 3

uf.union(4, 3)

assert uf.nsets == 2
assert uf.connected(0, 3) == False
assert uf.connected(4, 3) == True

p_expected = [1, 1, 3, 3, 3]
size_expected = [2, 2, 3, 3, 3]
for i in range(5):
    assert uf.find(i) == p_expected[i]
    assert uf.set_size(i) == size_expected[i]

uf.union(0, 3)

assert uf.nsets == 1
p_expected = [3] * 5
size_expected = [5] * 5
for i in range(5):
    assert uf.find(i) == p_expected[i]
    assert uf.set_size(i) == size_expected[i]
