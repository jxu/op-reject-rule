# Find 1-D recurrences:
# A(m+2,n) = 3 A(m+1,n) + A(m,n)
# A(m,n+2) = A(m,n+1) + 3 A(m,n)
#
# The matrix form is like
# [3 1]^m [A(1,n)] = [A(m+1,n)] and [1 3]^n [A(m,1)] = [A(m,n+1)]
# [1 0]   [A(0,n)]   [A(m,n)  ]     [1 0]   [A(m,0)]   [A(m,n)  ]
#
# Shortcut: since we are interested in m,n values that are Fibonacci,
# Multiply the last two matrix powers to compute the next matrix power.
# Generally: large values can be computed by exponentiation by squaring.
#
# Plan for each A(m,n):
# Find A(m,0) from A(0,0) and A(1,0), A(m,1) from A(0,1) and A(1,1)
# Find A(m,n) from A(m,0) and A(m,1)

import numpy as np
from number import fib_list


mod = 1123581313
F = fib_list(50)

I = np.eye(2, dtype=np.int64)

def S(k):
    s = 0
    M0 = I
    M1 = np.array([[3,1],[1,0]], dtype=np.int64)
    for i in range(2, k+1):
        # use last two M fib powers to find next M fib power
        M0, M1 = M1, (M0 @ M1) % mod

        # Trick: find M1 * [A(0,1),A(1,1)] and M1 * [A(1,0),A(0,0)] together
        # to get [A(m,1), A(m,0)]
        A0 = np.array([[2,1],[1,0]], dtype=np.int64)
        Am = (M1 @ A0)[1,:] % mod

        N0 = I
        N1 = np.array([[1,3],[1,0]], dtype=np.int64)
        for j in range(2, k+1):
            N0, N1 = N1, (N0 @ N1) % mod

            amn = (N1 @ Am)[1]
            s = (s + amn) % mod
    return s

print(S(50))


