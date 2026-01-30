# brute force?
from number import linear_sieve, linear_sieve_factors, divisors

M = 25_000_000

lp = linear_sieve(M)

s = 0

# trivial cases
a = 1
for b in range(1, M):
    c = b
    if a + b + c <= M:
        #print(a, b, c)
        s += 1

for a in range(2, M//3):
    am1, ap1 = a - 1, a + 1
    am1_factors = linear_sieve_factors(lp, am1)
    ap1_factors = linear_sieve_factors(lp, ap1)

    factors = am1_factors + ap1_factors

    divs = divisors(factors)
    #print(am1_factors, ap1_factors)
    #print(am1 * ap1, divs)

    for x in divs:
        y = (am1) * ap1 // x

        if (y + x) % 2: continue
        
        c = (x + y) // 2
        b = (y - x) // 2

        if a + y <= M and a <= b:
            print(a, b, c)
            #assert a*a + b* b == c*c + 1
            s += 1

print(s)
        
