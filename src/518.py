# b'^2 = a' * c'
import number
def S(n):
    s = 0
    primes = number.sieve(n)
    sp = set(primes)

    for b in primes:
        b1 = b + 1
        for a in primes:
            if a >= b: break

            a1 = a + 1
            if a1 < b1**2 / n: continue

            if b1**2 % a1 == 0:
                c1 = (b1**2 // a1)
                c = c1 - 1
                if c in sp:
                    print(a, b, c)
                    s += a + b + c

    return s

print(S(10**8))
