from functools import cache 
from bisect import bisect

cubes = [i**3 for i in range(10**6)]

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
    #print(k, q, r)

    return k*(q-1)*q//2 + q*S(k) + r*q + S(r)

# r = 0
# for i in range(101):
#     print(i,r,S(i))
#     r += d(i)


for k in range(int(10**(17/3))+1):
    print(k, S(k**3))

print(S(10**17))