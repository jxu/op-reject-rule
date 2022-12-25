# DP on paths, column by column
# path[i1,j] is current cell to compute
# find best path in column of cells of last col path[i0][j-1] plus
# sum of path[i0,j] to path[i1,j]
# ex for matrix
# [[5, 5, 1, 1],
#  [1, 5, 1, 5],
#  [1, 1, 1, 5],
#  [5, 5, 5, 5]]
# the best path sums are
# [[5, 10, 5, 6]
#  [1, 6, 4, 9]
#  [1, 2, 3, 8]
#  [5, 7, 8, 13]]

import csv
N = 80
with open("p082_matrix.txt", 'r') as f:
    matrix = [list(map(int, row)) for row in csv.reader(f)]
path = [[0] * N for _ in range(N)]

for i in range(N): path[i][0] = matrix[i][0]

for j in range(1, N):
    for i1 in range(N):
        min_col_path = 1e9
        for i0 in range(N):
            col_path = path[i0][j-1] + \
                sum(matrix[i2][j] for i2 in range(min(i0,i1), max(i0,i1)+1))
            min_col_path = min(min_col_path, col_path)
        path[i1][j] = min_col_path

print(min(path[i][N-1] for i in range(N)))
