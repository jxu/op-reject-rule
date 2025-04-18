
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
#print(matrix_powmod(A, 1, M))

def a(m,n):
    # am0 = a(m,0)
    # am1 = a(m,1)
    y = np.array([1,0], dtype=np.int64)  # [A(1,0), A(0,0)]
    z = np.array([2,1], dtype=np.int64)
    am0 = (matrix_powmod(A, m, M) @ y)[1] % M
    am1 = (matrix_powmod(A, m, M) @ z)[1] % M

    z1 = np.array([am1, am0], dtype=np.int64)

    amn = (matrix_powmod(B, n, M) @ z1)[1] % M

    return amn

from number import fib_list

F = fib_list(50)

def S(k):
    s = 0
    for i in range(2, k+1):
        for j in range(2, k+1):
            s = (s + a(F[i], F[j])) % M
    return s

print(S(50))


