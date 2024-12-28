"""
Simple telescoping sum from observing a_{2n} + a_{2n+1} = 3 a_n - 3 a_{n+1}
S(2n+1) = 1 + 3 a_1 - 3 a_{n+1} = 4 - 3 a_{n+1}
S(2n) = S(2n+1) - a_{2n+1} 
"""
from functools import cache  # optional

@cache
def a(n):
    if n == 1: return 1
    if n % 2 == 0: return 2 * a(n//2)
    else: return a(n//2) - 3 * a(n//2 + 1)

def S(N):
    if N % 2: return 4 - 3 * a(N//2 + 1)
    else: return S(N+1) - a(N+1)

print(S(10**12))
