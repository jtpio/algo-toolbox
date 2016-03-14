import random
from priority_queue import PriorityQueue

# Test the priority queue returns the elements in ascending order of priority

pq = PriorityQueue()
N = 20
ordered = list(range(N))
shuffled = list(range(N))
random.shuffle(shuffled)

for x in shuffled:
    pq.add(x, x)

popped = []
while not pq.is_empty():
    popped.append(pq.pop())

assert ordered == popped


# Test the priority queue returns the elements in descending order of priority

pq = PriorityQueue()
ordered = list(range(N))[::-1]  # reversed order
shuffled = list(range(N))
random.shuffle(shuffled)

for x in shuffled:
    pq.add(x, -x)  # use '-' to change the priority

popped = []
while not pq.is_empty():
    popped.append(pq.pop())

assert ordered == popped
