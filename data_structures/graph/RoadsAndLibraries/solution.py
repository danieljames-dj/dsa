from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, n, roads):
        self.nodes = range(1, n+1)
        self.edges = defaultdict(set)
        for a,b in roads:
            self.edges[a].add(b)
            self.edges[b].add(a)

def getClusterCount(g):
    visited = set()
    clusters = 0
    for node in g.nodes:
        if node in visited: continue
        clusters += 1
        Q = deque()
        Q.appendleft(node)
        while Q:
            cur = Q.pop()
            for edge in g.edges[cur]:
                if edge in visited: continue
                visited.add(edge)
                Q.appendleft(edge)
    return clusters

t = int(input())
for _ in range(t):
    n, m, c_lib, c_road = [int(x) for x in input().split()]
    roads = [[int(x) for x in input().split()] for _ in range(m)]
    if (c_road > c_lib):
        print(c_lib * n)
    else:
        g = Graph(n, roads)
        count = getClusterCount(g)
        print(c_lib * count + c_road * (n - count))