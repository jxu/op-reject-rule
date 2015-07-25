from number import dijkstra

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
