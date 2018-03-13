import numpy as np
from number import sieve

primes = sieve(1234)

# naive implementation
def exponent_array(n):
    arr = np.zeros(len(primes), dtype=int)
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n //= primes[i]
            arr[i] += 1

        if n == 1: break  # Done factoring

    if n != 1:
        print("none")
        return None  # Too large prime factor
    return arr


# Row-reduce binary matrix
def binary_rr(m):
    rows, cols = m.shape
    for k in range(min(rows, cols)):
        # Swap with pivot if diagonal is 0
        if m[k,k] == 0:
            for i in range(k+1, rows):
                if m[i,k] == 1:
                    m[i], m[k] = m[k].copy(), m[i].copy()  # Swap rows
                    break

        # For rows below pivot, subtract row
        for i in range(k+1, rows):
            if m[i,k]: m[i] ^= m[k]

    return m


def C(a, b):
    m = np.zeros([0, len(primes)], dtype=int)
    for n in range(a, b+1):
        arr = exponent_array(n)
        if not arr is None:
            m = np.insert(m, 0, arr % 2, axis=0)

    print(m.shape)

    rr_m = binary_rr(m)
    #np.set_printoptions(threshold=np.nan)
    #print(rr_m)
    nullity = int(np.sum(~rr_m.any(axis=1)))  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1


print(C(1000, 1234))