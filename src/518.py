# brute force after 165 min
# b'^2 = a' * c'
from number import sieve, factor, divisors

def S(n):
    s = 0
    primes = sieve(n)
    sp = set(primes)

    for b in primes:
        b1 = b + 1
        pps = factor(b1**2, primes)
        divs = sorted(divisors(pps))
        for a1 in reversed(divs):
            c1 = b1**2 // a1
            a = a1 - 1
            c = c1 - 1
            if c >= n: break
            if c1 > b1 and a in sp and c in sp:
                print(a, b, c)
                s += a + b + c

    return s

print(S(10**6))


