# string operations correspond to quaternion group operations
# via mapping x -> i, y -> k, z -> j
# the sign encodes the parity of the steps taken
from collections import Counter

# quick-n-dirty quaternion group:
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


def F(N):
    a = [0] * (50*N + 50)
    b = a[:]
    for i in range(len(a)):
        a[i] = (8888 * a[i-1]) % 888_888_883 if i > 0 else 88_888_888
        b[i] = a[i] % 3

    c = [0] * N  # start with 1s
    for i in range(N):
        for j in range(50*i, 50*i+50):
            # b[j] = 0 -> x -> i
            # b[j] = 1 -> y -> k
            # b[j] = 2 -> z -> j
            r = [2, 6, 4][b[j]]

            c[i] = MUL_TABLE[c[i]][r]

    counter = Counter(c)
    return sum(counter[k] * counter[INV_TABLE[k]] for k in counter)

print(F(10**6))
