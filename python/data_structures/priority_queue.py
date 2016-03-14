import itertools
from heapq import heappush, heappop


class PriorityQueue:
    '''
    Priority Queue implementation based. Based on:
    https://docs.python.org/3.5/library/heapq.html#priority-queue-implementation-notes
    '''
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.removed = -1
        self.counter = itertools.count()

    def add(self, task, priority=0):
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.removed

    def pop(self):
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.removed:
                del self.entry_finder[task]
                return task
        raise KeyError('Priority Queue is empty')

    def is_empty(self):
        return self.count() == 0

    def count(self):
        return len(self.pq)
