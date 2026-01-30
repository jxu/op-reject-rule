# brute force: rearranging as a^2 - 1 = c^2 - b^2
# factor as (a - 1) (a + 1) = (c - b) (c + b)
# combining factors of (a-1) (a+1), pick divisors x = c-b, y = c+b

# From thread: actually, pythagorean tree triples works too!
# See Problem 224
from collections import Counter
from number import linear_sieve, linear_sieve_factors, divisors

def f(M):
    lp = linear_sieve(M)

    # trivial cases have a = 1, b = c
    s = (M - 1) // 2

    # Avoid doing extra work by storing a+1 factors for later use
    # But not storing factorizations for entire a range
    am1_factors = Counter()
    a_factors = Counter([2])

    for a in range(2, M//3):
        ap1_factors = linear_sieve_factors(lp, a+1)

        # combine as dict, although gcd(a-1, a+1) = 1 or 2
        factors = am1_factors + ap1_factors
        divs = divisors(factors)  # unordered

        for x in divs:
            y = (a - 1) * (a + 1) // x

            if (y + x) % 2: continue
            
            c = (x + y) // 2
            b = (y - x) // 2

            if a + y <= M and a <= b:
                #print(a, b, c)
                s += 1

        # shift stored factors
        am1_factors, a_factors = a_factors, ap1_factors

    return s

print(f(25_000_000))
            
