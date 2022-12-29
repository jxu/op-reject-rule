# divisibility method of a from dev_random:
# let a', b', c' = a+1, b+1, c+1
# b' = a' j / k, c' = a' j^2 / k^2
# assuming gcd(j,k) = 1, k^2 divides a'
# search through divisors of a' for squares
# benchmark: 55s
from number import sieve, factor, divisors
from math import gcd

def S(n):
    s = 0
    primes = sieve(n)
    sp = set(primes)
    squares = set([k**2 for k in range(1, round(n**0.5)+1)])

    for a in primes:
        a1 = a + 1
        pp = factor(a1, primes)
        for k2 in divisors(pp):
            if k2 in squares:
                k = round(k2 ** 0.5)
                for j in range(k+1, n):
                    if gcd(j, k) != 1: continue
                    b1 = a1 * j // k
                    c1 = b1 * j // k
                    if c1 > n: break
                    b, c = b1 - 1, c1 - 1
                    if b in sp and c in sp:
                        #print(f"{j}/{k}", a, b, c)
                        s += a + b + c
    return s

print(S(10**8))


