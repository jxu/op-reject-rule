from functools import cache

# represent elements 1, -1, i, -i, j, -j, k, -k as 0 thru 7

MUL_TABLE = [
    [0, 1, 2, 3, 4, 5, 6, 7],  # 1
    [1, 0, 3, 2, 5, 4, 7, 6],  # -1
    [2, 3, 1, 0, 6, 7, 5, 4],  # i
    [3, 2, 0, 1, 7, 6, 4, 5],  # -i
    [4, 5, 7, 6, 1, 0, 2, 3],  # j
    [5, 4, 6, 7, 0, 1, 3, 2],  # -j
    [6, 7, 4, 5, 3, 2, 1, 0],  # k
    [7, 6, 5, 4, 2, 3, 0, 1],  # -k
]

# i^-1 = -i,  j^-1 = -j, k^-1 = -k
INV_TABLE = [0, 1, 3, 2, 5, 4, 7, 6]

@cache
def f(a, b, c, r):
    if a < 0 or b < 0 or c < 0:
        return 0
    if a == b == c == 0:
        return r == 0
    
    return (f(a-1, b, c, MUL_TABLE[r][3]) +
        f(a, b-1, c, MUL_TABLE[r][5]) + 
        f(a, b, c-1, MUL_TABLE[r][7]))

print(f(8, 8, 8, 0))

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            print(i, j, k, f(i, j, k, 0))
