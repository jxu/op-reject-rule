# string operations correspond to quaternion group operations
# via mapping x -> i, y -> k, z -> j
# the sign encodes the parity of the steps taken
from collections import Counter

# quick-n-dirty quaternion group:
# represent elements 1, -1, i, -i, j, -j, k, -k as 0 thru 7
P1, M1, PI, MI, PJ, MJ, PK, MK = range(8)


QMUL = [
    [P1, M1, PI, MI, PJ, MJ, PK, MK],  # 1
    [M1, P1, MI, PI, MJ, PJ, MK, PK],  # -1
    [PI, MI, M1, P1, PK, MK, MJ, PJ],  # i
    [MI, PI, P1, M1, MK, PK, PJ, MJ],  # -i
    [PJ, MJ, MK, PK, M1, P1, PI, MI],  # j
    [MJ, PJ, PK, MK, P1, M1, MI, PI],  # -j
    [PK, MK, PJ, MJ, MI, PI, M1, P1],  # k
    [MK, PK, MJ, PJ, PI, MI, P1, M1],  # -k
]

# i^-1 = -i,  j^-1 = -j, k^-1 = -k
QINV = [P1, M1, MI, PI, MJ, PJ, MK, PK]


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
            r = [PI, PK, PJ][b[j]]

            c[i] = QMUL[c[i]][r]

    counter = Counter(c)
    return sum(counter[k] * counter[QINV[k]] for k in counter)

print(F(10**6))
