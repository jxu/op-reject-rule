# To make more efficient
from __future__ import division
import numpy as np
from number import sieve

np.set_printoptions(threshold=np.nan)
primes = sieve(234567)

# naive implementation
def exponent_array(n):
    arr = np.zeros(len(primes), dtype=int)
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n //= primes[i]
            arr[i] += 1

        if n == 1: return arr  # Done factoring

    return np.full(len(primes), -1) # Too large prime factor


# Row-reduce binary matrix
def binary_rr(m):
    rows, cols = m.shape
    l = 0
    for k in range(min(rows, cols)):
        print(k)
        if l >= cols: break
        # Swap with pivot if m[k,l] is 0
        if m[k,l] == 0:
            found_pivot = False
            while not found_pivot:
                if l >= cols: break
                for i in range(k+1, rows):
                    if m[i,l]:
                        m[[i,k]] = m[[k,i]]  # Swap rows
                        found_pivot = True
                        break

                if not found_pivot: l += 1

        if l >= cols: break  # No more rows

        # For rows below pivot, subtract row
        for i in range(k+1, rows):
            if m[i,l]: m[i] ^= m[k]

        l += 1

    return m


def C(a, b):
    m = np.zeros([b-a+1, len(primes)], dtype=np.int8)
    for n in range(a, b+1):
        m[n-a] = exponent_array(n)

    m = m[m[:,0] != -1] % 2
    print(m.shape)

    rr_m = binary_rr(m)
    nullity = int(np.sum(~rr_m.any(axis=1)))  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1


print(C(1000000, 1234567))