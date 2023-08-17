from number import sieve
from math import log
primes = sieve(2 * 10**7)  # q log(2) + 2 log(q) <= logn

def C(logn):
    s = 0
    # two pointer method. could also binary search q
    i, j = 0, len(primes) - 1
    while i < j:
        p, q = primes[i], primes[j]
        while q*log(p) + p*log(q) > logn:
            j -= 1
            # can't have j < i here because we would've encountered it
            # when p, q = primes[j], primes[i] (?)
            q = primes[j]

        s += j - i
        print(p, q)
        i += 1
    return s


print(C(800800*log(800800)))