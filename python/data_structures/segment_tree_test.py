from segment_tree import SegmentTree

a = [18, 17, 13, 19, 15, 11, 20]
st = SegmentTree(a)

assert st.rmq(1, 3) == 2
assert st.rmq(3, 4) == 4
assert st.rmq(0, 0) == 0
assert st.rmq(0, 1) == 1

assert st.rmq(0, 6) == 5
assert st.rmq(4, 6) == 5

st.update(5, 100)

assert st.rmq(1, 3) == 2
assert st.rmq(3, 4) == 4
assert st.rmq(0, 0) == 0
assert st.rmq(0, 1) == 1

assert st.rmq(0, 6) == 2
assert st.rmq(4, 6) == 4
assert st.rmq(4, 5) == 4
