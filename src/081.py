# Classic DP problem
import csv
N = 80
with open("p081_matrix.txt", 'r') as f:
    matrix = [list(map(int, row)) for row in csv.reader(f)]

path = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i, j) == (0, 0): path[i][j] = matrix[i][j]
        elif i == 0:         path[i][j] = matrix[i][j] + path[i][j-1]
        elif j == 0:         path[i][j] = matrix[i][j] + path[i-1][j]
        else:                path[i][j] = matrix[i][j] + \
                                          min(path[i][j-1], path[i-1][j])

print(path[N-1][N-1])
