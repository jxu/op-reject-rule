from bisect import bisect 
from number import sieve
from functools import cache
from math import comb, isqrt
from itertools import accumulate

def test_prime_count():
    # A000720
    small_values = (0,0,1,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,8,8)
    for i in range(len(small_values)):
        assert prime_count(i) == small_values[i]

    # A006880
    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]


def icbrt(x):
    # https://cs.stackexchange.com/a/4841
    if x < 0: raise ValueError
    z0 = int(x**(1/3))
    for z in (z0+1, z0, z0-1):
        if z**3 <= x:
            return z



SIEVE_MAX = 10**7  # at least x^2/3
primes = sieve(SIEVE_MAX)  # 0-indexed prime list


small_primes = (2, 3, 5, 7, 11, 13, 17, 19)
C = len(small_primes) # should be <= a = pi(x^1/3)
Q = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

partial_sieve = [1] * (Q+1)
partial_sieve[0] = 0
for p in small_primes:
    for j in range(p, Q+1, p):
        partial_sieve[j] = 0

phi_C = list(accumulate(partial_sieve))
#print(phi_C)

def phi(y, b):
    #print("phi",y,b)
    if y < primes[b-1]:
        return 1 

    assert b >= C
    if b == C:
        return (y // Q) * phi_C[Q] + phi_C[y % Q] 

    return phi(y, b-1) - phi(y // primes[b-1], b-1)

@cache
def prime_count(x):
    if x < 1:
        raise ValueError

    if x <= SIEVE_MAX:
        return bisect(primes, x)

    a = prime_count(icbrt(x))  # rounding
    b = prime_count(isqrt(x))

    P2 = comb(a, 2) - comb(b, 2) 
    for j in range(a+1, b+1): 
        P2 += prime_count(x // primes[j-1])

    return a - P2 + phi(x, a) - 1



def f(n):
    primes = sieve(int(n**0.5))

    # Case 1: n = p^7
    count = prime_count(int(n**(1/7)))

    # Case 2: n = p^3 * q
    for p in primes:
        if p**3 > n: break
        q_max = n // (p**3)
        # Exclude case with p == q
        count += prime_count(q_max) - (q_max >= p)

    print("Starting case 3...")
    # Case 3: n = p*q*r, p < q < r
    for p_i in range(len(primes)):
        p = primes[p_i]
        if p**3 > n: break

        for q_i in range(p_i + 1, len(primes)):
            q = primes[q_i]
            if q > (n / p)**0.5: break  # max q when q = r so n = p * q^2
            print(p, q, n//(p*q))

            # q < r < n/pq, so add pi(n/pq) - pi(q)
            count += prime_count(n // (p*q)) - (q_i + 1)

    return count


#print(f(10**12))
print(prime_count(10**11))
