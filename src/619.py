from number import sieve, ceil_div
from collections import Counter



# Row-reduce binary matrix
def binary_rr(L, m, n):
    h = k = 0  # pivot row, col

    while h < m and k < n:
        if k < 10 or k % 1000 == 0: 
            print("pivot", k)
        #print(L)
        found_piv = False
        piv = None
        for i in range(h, m):
            if k in L[i]:
                found_piv = True
                piv = i
                break

        if not found_piv:
            k += 1
        else:
            L[piv], L[h] = L[h], L[piv]  # swap rows
            for i in range(h+1, m):
                if k in L[i]:
                    for j in L[h]:
                        if j in L[i]:
                            L[i].remove(j)
                        else:
                            L[i].append(j)

            h += 1
            k += 1

    return L





def C(a, b):
    primes = sieve(b)

    rows = b - a + 1
    cols = len(primes)

    print((rows, cols))

    m = [Counter() for _ in range(b-a+1)]
    for i in range(len(primes)):
        p = primes[i]  # prime and prime powers
        pp = p
        while pp <= b:
            for n in range(pp * ceil_div(a, pp), b+1, pp):
                #print(pp, n)
                m[n-a][i] += 1
            pp *= p

    print(m)
    print("done factoring")

    # remove all 0s rows (no small prime factors), set coef mod 2
    # convert to sparse format: list of rows
    # skip removing empty rows for now
    L = [[] for _ in range(rows)]
    
    for i in range(rows):

        for j in m[i]:  # keys
            if m[i][j] % 2: 
                L[i].append(j)

    print(L)
    print("done sparse")

    rr_m = binary_rr(L, rows, cols)
    print(m)
    nullity = sum(row == [] for row in rr_m)  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1

#print(C(40,55))
print(C(1000,1234))
#print(C(1000000,1234567))
