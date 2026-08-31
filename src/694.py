from number import sieve
from sortedcontainers import SortedList

primes = sieve(10**6)


    
def S(n):
    result = SortedList([1])

    # non-recursive version
    for p in primes:
        if p**3 > n: break

        new_res = []
        for x in result:
            y = p**3 * x
            if y > n: break

            while y <= n:
                new_res.append(y)
                y *= p


        for x in new_res:
            result.add(x)  # fast insert

    s = n
    for x in result:
        if x == 1: continue
        s += n // x
    return s

print(S(10**18))
