# Find 1-D recurrences:
# A(m+2,n) = 3 A(m+1,n) + A(m,n)
# A(m,n+2) = A(m,n+1) + 3 A(m,n)
# Large values can be computed by exponentiation by squaring.
# (Idea: use recursion on Fib m,n values instead of exp by squaring)
#
# Plan for each A(m,n):
# Find A(m,0) from A(0,0) and A(1,0)
# Find A(m,1) from A(0,1) and A(1,1)
# Find A(m,n) from A(m,0) and A(m,1)


import numpy as np

def matrix_powmod(A, k, M):
    r = np.eye(2, dtype=np.int64)
    while k:
        if k % 2:
            r = (r @ A) % M
        A = (A @ A) % M
        k >>= 1

    return r


M = 1123581313

A = np.array([[3,1],[1,0]], dtype=np.int64)
B = np.array([[1,3],[1,0]], dtype=np.int64)

from number import fib_list

F = fib_list(50)

def S(k):
    s = 0
    for i in range(2, k+1):
        m = F[i]

        y = np.array([1,0], dtype=np.int64)  # [A(1,0), A(0,0)]
        z = np.array([2,1], dtype=np.int64)
        am = matrix_powmod(A, m, M)
        am0 = (am @ y)[1] % M
        am1 = (am @ z)[1] % M

        z1 = np.array([am1, am0], dtype=np.int64)

        for j in range(2, k+1):
            n = F[j]
            amn = (matrix_powmod(B, n, M) @ z1)[1] % M
            s = (s + amn) % M
    return s

print(S(50))


