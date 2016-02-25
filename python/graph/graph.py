from collections import defaultdict, deque
from heapq import heappush, heappop


class Graph:
    '''
    Very simple abstraction for undirected graphs.
    The main purpose of this graph representation is to be able to edit it
    quickly for custom needs.
    Use Networkx for more advanced graphs.

    The graph is stored as an adjacency list.
    The graph supports weights. Default to 1 for the weight if no weight is
    provided.
    '''

    def __init__(self):
        self.g = defaultdict(list)

    def _max_distance(self, dists):
        return max(dists, key=lambda x: dists[x])

    def _print(self):
        for u, vs in self.g.items():
            print(u, ':', vs)

    def add_node(self, node):
        if node not in self.g:
            self.g[node] = []

    def add_edge(self, u, v, weight=1):
        self.g[u].append((v, weight))
        self.g[v].append((u, weight))

    def degree(self, node):
        return len(self.g[node])

    def bfs(self, source):
        q = deque()
        q.append((source, 0))
        dists = {source: 0}

        while len(q) > 0:
            u, dist = q.popleft()
            neighbors = [(v, w) for v, w in self.g[u] if v not in dists]
            for v, w in neighbors:
                dists[v] = dist + w
                q.append((v, dist + w))

        return dists

    def dijkstra(self, source, target):
        q = []
        heappush(q, (0, source))
        dists = {source: 0}
        parent = {source: None}

        while len(q) > 0:
            dist, u = heappop(q)
            if u == target:
                path = []
                while u is not None:
                    path.append(u)
                    u = parent[u]
                # Reverse the order of the path
                return path[::-1]

            neighbors = [(v, w) for v, w in self.g[u]
                         if v not in dists or dist + w < dists[v]]
            for v, w in neighbors:
                dists[v] = dist + w
                parent[v] = u
                heappush(q, (dist + w, v))

        return []

    def diameter_center(self):
        '''
        Calculate the diameter and the center of the graph
        '''
        # select the first node of the graph
        source = next(iter(self.g))
        dists = self.bfs(source)
        start = self._max_distance(dists)
        dists_2 = self.bfs(start)
        end = self._max_distance(dists_2)
        path = self.dijkstra(start, end)

        diameter = dists_2[end]
        center = path[len(path) // 2] if len(path) > 0 else None

        return diameter, center
