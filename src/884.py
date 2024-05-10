from functools import cache 
from bisect import bisect_left

cubes = [i**3 for i in range(10**6)]

def smaller_cube(n):
    return cubes[bisect_left(cubes,n)-1]

@cache
def S(N):
    if N <= 1: return 0

    k = smaller_cube(N)
    # original method
    # q, r = N//k, N%k
    # return k*(q-1)*q//2 + q*S(k) + r*q + S(r)
    return S(k) + S(N-k) + (N - k)

for k in range(int(10**(17/3))+1):
    S(k**3)

print(S(10**17))