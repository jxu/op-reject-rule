# DP from looking at last piece placed, which is uniformly distributed
# For the final product, sub-segments can be considered independently
# e(N) = (2N-1)N (1/N sum_{i=1..N} e(i-1) e(N-i)) with N canceling out
from functools import cache

@cache
def e(N):
    if N == 0: return 1
    return (sum(e(i-1)*e(N-i) for i in range(1,N+1)) * (2*N-1)) % 987654319

print(e(100))