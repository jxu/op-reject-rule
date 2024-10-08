# TODO: proper explanation
# 2:10 with cache

from number import sieve, prod, icbrt
from functools import cache
from math import comb, isqrt
from itertools import accumulate

class PrimeCount:


    def __init__(self, x):

        self.SIEVE_MAX = 5 * 10**7  # at least x^2/3
        self.primes = sieve(self.SIEVE_MAX)  # 0-indexed primes up to x^2/3

        print("sieve done")


        small_primes = (2, 3, 5, 7, 11, 13, 17)
        self.C = C = len(small_primes) # should be <= a = pi(x^1/3)
        self.Q = Q = prod(small_primes)


        partial_sieve = [1] * (Q+1)
        partial_sieve[0] = 0
        for p in small_primes:
            for j in range(p, Q+1, p):
                partial_sieve[j] = 0

        self.phi_C = list(accumulate(partial_sieve))

        # more efficient to get from the sieve()
        prime_count_ind = [0]*(self.SIEVE_MAX+1)
        for p in self.primes:
            prime_count_ind[p] = 1

        # a little faster than binary search
        self.prime_count_small = list(accumulate(prime_count_ind))


        self.a = self.prime_count_small[icbrt(x)]  # rounding
        self.b = self.prime_count_small[isqrt(x)]



    def phi(self, y, b):
        #print("phi",y,b)
        C, Q = self.C, self.Q
        if y < self.primes[b-1]:
            return 1

        assert b >= C
        if b == C:
            return (y // Q) * self.phi_C[Q] + self.phi_C[y % Q]

        return self.phi(y, b-1) - self.phi(y // self.primes[b-1], b-1)


    def __call__(self, x):
        #print("pi", x)
        if x < 1:
            raise ValueError

        if x <= self.SIEVE_MAX:
            return self.prime_count_small[x]

        a, b = self.a, self.b

        P2 = comb(a, 2) - comb(b, 2)
        for j in range(a+1, b+1):
            # No recursive call
            P2 += self.prime_count_small[x // self.primes[j-1]]

        return a - P2 + self.phi(x, a) - 1


    def test_prime_count(self):
        prime_count = self.__call__(10**7)

        # A000720
        small_values = (0,0,1,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,8,8)
        for i in range(len(small_values)):
            assert prime_count(i) == small_values[i]

        # A006880
        powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579)

        for i in range(len(powers_10)):
            assert prime_count(10**i) == powers_10[i]



def f(n):
    prime_count = PrimeCount(n)
    primes = prime_count.primes

    # Case 1: n = p^7
    count = prime_count(int(n**(1/7)))

    i = 0
    while (p := primes[i])**3 <= n:
        # Case 2: n = p^3 * q, Exclude case with p == q
        q_max = n // (p**3)
        count += prime_count(q_max) - (q_max >= p)

        # Case 3: n = p*q*r, p < q < r
        j = i + 1
        while (q := primes[j])**2 * p <= n:
            #print(p, q)
            # q < r < n/pq, so add pi(n/pq) - pi(q)
            count += prime_count(n // (p*q)) - (j + 1)
            j += 1
        i += 1

    #print(prime_count.phi.cache_info())
    return count


print(f(10**12))
