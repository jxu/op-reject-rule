# S(n) = (D(1) + ... + D(k-1)) + (D(k) + ... + D(n-1)) for k smallest cube < n
# = S(k) + ((D(0) + 1) + ... + (D(n-1-k) + 1))
# = S(k) + S(n-k) + (n - k) recursive

# My original approach did more arithmetic computing exactly many copies of
# S(k) to use and adjust for remainder S(n-k).
# q, r = N//k, N%k
# S(n) = k*q*(q-1)//2 + q*S(k) + r*q + S(r)
# I didn't realize the simpler recursion would run in time, but for
# S(n), S(n-k), S(n-2k), ... there are only at most n/k calls.

from functools import cache
from bisect import bisect_left

cubes = [i**3 for i in range(10**6)]

# no floating point error
def smaller_cube(n):
    return cubes[bisect_left(cubes,n)-1]

@cache
def S(N):
    if N <= 1: return 0
    k = smaller_cube(N)
    return S(k) + S(N-k) + (N - k)

# cache cubes to avoid recursion limit (at least S(k) is cached)
for n in range(int(10**(17/3))+1):
    S(n**3)

print(S(10**17))