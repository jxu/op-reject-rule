# Classic DP problem
import csv
from copy import deepcopy
N = 80
with open("p081_matrix.txt", 'r') as f:
    matrix = [list(map(int, row)) for row in csv.reader(f)]

path_sum = deepcopy(matrix)
for i in range(N):
    for j in range(N):
        if (i, j) == (0, 0): continue
        elif i == 0:         path_sum[i][j] += path_sum[i][j-1]
        elif j == 0:         path_sum[i][j] += path_sum[i-1][j]
        else:                path_sum[i][j] += min(path_sum[i][j-1],
                                                   path_sum[i-1][j])

print(path_sum[N-1][N-1])
