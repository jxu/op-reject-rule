# Brilliant puzzle.

from number import sieve

def a(n, s): return 3*n**2 - 3*n + 2 + n*s

primes = set(sieve(10**6))
PD3 = [1]

for n in range(1, 10**5):
    # First tile: a(n,0)
    if 6*n+1 in primes and 6*n-1 in primes and 12*n+5 in primes:
        print(a(n, 0))
        PD3.append(a(n, 0))

    # Corner tiles: a(n,s)
    for s in range(1, 6):
        prime_diffs = 0
        cases = (6*(n-1)+s, 6*n+s, 6*n+s+1, 6*n-s-1)
        for case in cases:
            if case in primes: prime_diffs += 1

        if prime_diffs >= 3:
            print(a(n, s))
            PD3.append(a(n, s))

    # Last tile: a(n+1,0)-1
    if n > 1:
        if 6*n-1 in primes and 12*n-7 in primes and 6*n+5 in primes:
            print(a(n+1, 0)-1)
            PD3.append(a(n+1, 0)-1)


print(PD3[2000-1])