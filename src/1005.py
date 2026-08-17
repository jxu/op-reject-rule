import sys
from number import sieve
from functools import cache

sys.setrecursionlimit(3000)
primes = sieve(2026)

@cache
def f(n, min_i):
    # count increasing tuples that sum to n, using only primes[i] and greater
    if n < 0: return 0
    if n == 0: return 1
    s = 0
    for i in range(min_i, len(primes)):
        if (n - primes[i] < 0): break
        s += f(n - primes[i], i+1)

    return s


def search(n, min_i, target):
    if n == 0: return 1

    print(n, min_i, target)

    s = 0

    for i in range(min_i, len(primes)):

        if target < s + f(n - primes[i], i+1):
            #print("output", primes[i])
            # compute product directly here
            return (primes[i] * search(n - primes[i], i+1, target - s)) % 10**9
        else: 
            s += f(n - primes[i], i+1) 

    raise ValueError

def mpl(n):

    # median index for list of size n: (n-1)/2
    return search(n, 0, (f(n, 0)-1) // 2)


print(mpl(2026))

