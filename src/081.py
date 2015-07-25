with open("p081_matrix.txt", 'r') as f:
    matrix = f.read().splitlines()
    matrix = [list(map(int, row.split(','))) for row in matrix]

path = matrix[:]

for i in range(80):
    for j in range(80):
        if (i, j) == (0, 0):    continue
        if i == 0:              path[i][j] += path[i][j-1]
        elif j == 0:            path[i][j] += path[i-1][j]
        else:                   path[i][j] += min(path[i][j-1], path[i-1][j])

print(path[79][79])