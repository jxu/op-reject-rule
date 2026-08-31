# I've misread this problem 3 times, thinking about things like divisor
# function and inclusion-exclusion, when all that's needed is to generate
# cube-full numbers and count how many multiples fit within n, because
# those correspond exactly to the cube-full divisors of 1 through n.

# Previously I had a more involved breadth-first approach with 
# SortedList because I had each level correspond to multiplying by 1 or p^3+
# for every prime p, but a depth-first recursion where each level is how many
# distinct prime powers are multipled together is much shallower and simpler.
from number import sieve

primes = sieve(10**6)

n = 10**18
def f(c, i):
    s = n // c

    for j in range(i, len(primes)):
        y = c * primes[j]**3
        # important: exit loop early if starting y is already too big
        if y > n: break
       
        while y <= n: 
            s += f(y, j+1)
            y *= primes[j]
    
    return s

print(f(1, 0))

