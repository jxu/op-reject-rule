from functools import cache

@cache
def a(n):
    if n == 1: return 1
    if n % 2 == 0: return 2 * a(n//2)
    else: return a(n//2) - 3 * a(n//2 + 1)

def S(N):
    if N % 2: return 4 - 3 * a(N//2 + 1)
    else: return S(N+1) - a(N+1)

print(S(10**12))
