from number import sieve
from math import log
primes = sieve(2 * 10**7)  # q log(2) + 2 log(q) <= logn

def C(logn):
    s = 0
    for i in range(len(primes)):
        p = primes[i]
        print(p)
        # could also use binary search on q
        for j in range(i+1, len(primes)):
            q = primes[j]
            if q*log(p) + p*log(q) > logn: break
            #print(p, q, q*log(p) + p*log(q))
            s += 1
    return s

print(C(800800*log(800800)))