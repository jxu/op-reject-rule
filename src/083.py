def dijkstra(graph, start):
    """Dijkstra's algorithm using heaps.

    Test using g = {0:{1:2}, 1:{0:2, 2:6}, 2:{1:6}}
    Credit: Janne Karila
    """
    from heapq import heappush, heappop

    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    return A

with open("p083_matrix.txt", 'r') as f:
    matrix = f.read().splitlines()
    matrix = [list(map(int, row.split(','))) for row in matrix]

def f(i, j):  # flatten
    return 80*i + j

g = {}
for i in range(80):
    for j in range(80):
        neighbors = {}
        if i > 0:   neighbors[f(i-1, j)] = matrix[i-1][j]
        if i < 79:  neighbors[f(i+1, j)] = matrix[i+1][j]
        if j > 0:   neighbors[f(i, j-1)] = matrix[i][j-1]
        if j < 79:  neighbors[f(i, j+1)] = matrix[i][j+1]

        g[f(i, j)] = neighbors

d = dijkstra(g, 0)
print(matrix[0][0] + d[-1])
