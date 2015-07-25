# Who needs clever row insertion when you have Dijkstra?

from number import dijkstra

with open("p082_matrix.txt", 'r') as f:
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
        if j < 79:  neighbors[f(i, j+1)] = matrix[i][j+1]

        g[f(i, j)] = neighbors

min_path = 10**8
for start in range(80):
    d = dijkstra(g, 80*start)
    min_path = min(matrix[start][0] + min(d[x] for x in range(79, 80*80, 80)), min_path)

print(min_path)