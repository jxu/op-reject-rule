# b'^2 = a' * c'
from number import sieve, factor, divisors

def S(n):
    s = 0
    primes = sieve(n)
    sp = set(primes)

    for b in primes:
        b1 = b + 1
        pp = factor(b1, primes)
        # generate all divisors of b1
        divs = divisors(pp)
        print(b1, divs)
        for a1 in divs:
            a = a1 - 1
            c1 = b1**2 // a1
            c = c1 - 1
            if b1 < c1 and a in sp and c in sp:
                print(a, b, c)
                s += a + b + c


    return s

print(S(100))


