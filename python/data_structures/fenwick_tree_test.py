from fenwick_tree import FenwickTree

ft = FenwickTree(10)

ft.adjust(2, 1)
ft.adjust(4, 1)
ft.adjust(5, 2)
ft.adjust(6, 3)
ft.adjust(7, 2)
ft.adjust(8, 1)
ft.adjust(9, 1)

assert ft.rsq(1, 1) == 0
assert ft.rsq(1, 2) == 1
assert ft.rsq(1, 6) == 7
assert ft.rsq(1, 10) == 11
assert ft.rsq(3, 6) == 6

ft.adjust(5, 2)

assert ft.rsq(1, 10) == 13
