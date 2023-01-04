# Dijkstra's algorithm (using simple array instead of priority queue)
# runtime O(|V|^2 + |E|) = O(n^4)

import csv
N = 80
INF = 1000000

with open("p082_matrix.txt", 'r') as f:
    matrix = [list(map(int, row)) for row in csv.reader(f)]

graph = {}
dist = {}
mark = {}
for i in range(N):
    for j in range(N):
        # graph stored as dict of dicts
        # {s: {t1:v1, t2:v2, ...}, ...}
        graph[(i, j)] = {}
        dist[(i, j)] = INF
        mark[(i, j)] = False
        if i > 0:   graph[(i,j)][(i-1,j)] = matrix[i][j]
        if i < N-1: graph[(i,j)][(i+1,j)] = matrix[i][j]
        if j > 0:   graph[(i,j)][(i,j-1)] = matrix[i][j]
        if j < N-1: graph[(i,j)][(i,j+1)] = matrix[i][j]

dist[(0,0)] = 0

for k in range(N*N):
    v = None  # next vertex to consider
    # loop through all vertices to find v = argmin_w dist[w]
    for i in range(N):
        for j in range(N):
            w = (i,j)
            if not mark[w] and (v is None or dist[w] < dist[v]):
                v = w

    mark[v] = True  # visit v
    # loop through edges
    for target, length in graph[v].items():
        if dist[v] + length < dist[target]:
            dist[target] = dist[v] + length

print(dist[(N-1,N-1)] + matrix[N-1][N-1])
