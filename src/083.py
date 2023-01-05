# Dijkstra's algorithm (using priority queue)
# runtime O(|E|log|V|) = O(N^2 log N)
from heapq import heappush, heappop

import csv
N = 80
INF = 1000000

with open("p082_matrix.txt", 'r') as f:
    matrix = [list(map(int, row)) for row in csv.reader(f)]

graph = {}
dist = {}
queue = [(0,0)]

for i in range(N):
    for j in range(N):
        # graph stored as dict of edges: (target, dist) pairs
        # {s1: [(t1,d1), (t2,d2), ...], ...}
        graph[(i, j)] = []
        dist[(i, j)] = INF
        # assign to edge the value of the *source* node
        if i > 0:   graph[(i,j)].append(((i-1,j), matrix[i][j]))
        if i < N-1: graph[(i,j)].append(((i+1,j), matrix[i][j]))
        if j > 0:   graph[(i,j)].append(((i,j-1), matrix[i][j]))
        if j < N-1: graph[(i,j)].append(((i,j+1), matrix[i][j]))

dist[(0,0)] = 0
queue =[(0, (0,0))]  # stores (dist, vertex) order for sorting
while queue:
    d, v = heappop(queue)  # min-heap
    if d != dist[v]: continue  # skip old vertices

    # loop through edges
    for target, length in graph[v]:
        if dist[v] + length < dist[target]:
            dist[target] = dist[v] + length
            heappush(queue, (dist[target], target))

print(dist[(N-1,N-1)] + matrix[N-1][N-1])
