import numpy as np
from number import sieve

primes = sieve(55)

# Row-reduce binary matrix
def binary_rr(A):
    m, n = A.shape
    h = k = 0  # pivot row, col

    while h < m and k < n:
        print("pivot", k)
        print(A)
        found_piv = False
        piv = None
        for i in range(h, m):
            if A[i,k]:
                found_piv = True
                piv = i
                break

        if not found_piv:
            k += 1
        else:
            A[[h,piv]] = A[[piv,h]]  # swap rows
            for i in range(h+1, m):
                f = A[i,k]
                #print(f)
                A[i,k] = 0
                for j in range(k+1, n):
                    A[i,j] ^= A[h,j] & f

            h += 1
            k += 1

    return A





def C(a, b):
    m = np.zeros([b-a+1, len(primes)], dtype=np.int8)
    for i in range(len(primes)):
        p = primes[i]  # prime and prime powers
        pp = p
        while pp <= b:
            for n in range(pp * (a//pp), b+1, pp):
                
                if n < a: continue  # ceil div
                #print(pp, n)
                m[n-a,i] += 1
            pp *= p
            

    print(m.shape)

    # remove all 0s rows (no small prime factors), set coef mod 2
    m = m[~ np.all(m == 0, axis=1)] % 2
    print("after removing rows")
    print(m)

    rr_m = binary_rr(m)
    #print(m)
    nullity = int(np.sum(~rr_m.any(axis=1)))  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1


print(C(40, 55))
