from functools import cache 
from bisect import bisect

cubes = [i**3 for i in range(100)]

def icbrt(n):
    return cubes[bisect(cubes,n)-1]

def d(n):
    r = 0
    while n:
        k = icbrt(n)
        n -= k
        r += 1

    return r

@cache
def S(N):
    #print(N)
    if N <= 1: return 0
    k = icbrt(N-1)
    q, r = N//k, N%k

    return (q-1)*q//2 + q*S(k) + r*q + S(r) 

r = 0
for i in range(101):
    print(i,r,S(i))
    r += d(i)

#print(64**(1/3))
