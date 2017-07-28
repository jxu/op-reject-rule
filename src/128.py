# Brilliant puzzle.
# Most tiles have two neighbors that have difference 1 and can be ignored.
# The only tiles that don't are the first and last tile of a ring (ex. 8 and 19)
# For all tiles (edges AND corners) except for the first and last tiles, the
# differences between neighbors will be 2 ignored, 2 evens, and 2 odds. Thus
# tile(x) can't be 3.

from number import sieve

def a(n): return 3*n**2 - 3*n + 2  # Formula for first tile in ring of size n

primes = set(sieve(10**6))
PD3 = [1]

for n in range(1, 10**5):
    # First tile: a(n)
    if 6*n+1 in primes and 6*n-1 in primes and 12*n+5 in primes:
        print(n, a(n))
        PD3.append(a(n))

    # Last tile: a(n+1)-1
    if n > 1:
        if 6*n-1 in primes and 12*n-7 in primes and 6*n+5 in primes:
            print(n, a(n+1)-1)
            PD3.append(a(n+1)-1)


print(PD3[2000-1])