
# - max prime b/2, sparse matrix 217706 x 60415: 4m40s
# - max pf b-a, sparse 197120 x 20794: 2m25s

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
            for i in range(h+1, m):  # rows below pivot h
                if k in L[i]:
                    for j in L[h]:
                        if j in L[i]:  # add or remove entry in row i
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

    #print((rows, cols))
    # factor all n
    m = [Counter() for _ in range(b-a+1)]
    for i in range(len(primes)):
        p = primes[i]  # prime and prime powers
        pp = p
        while pp <= b:
            for n in range(pp * ceil_div(a, pp), b+1, pp):
                #print(pp, n)
                m[n-a][i] += 1
            pp *= p

    #print(m)
    print("done factoring")

    # ignore any n with too large factor, set coef mod 2
    # convert to sparse format: list of rows
    # skip removing empty rows for now
    L = []
    max_col = 0
    for i in range(rows):


        if any(primes[pi] > b-a for pi in m[i]):
            continue
        #if len(m[i]) == 0:
        #    continue
        L.append([])
        for j in m[i]:  # keys
            max_col = max(max_col, j)
            if m[i][j] % 2: 
                L[-1].append(j)

    #print(L)
    print("done sparse")
    rows = len(L)
    cols = max_col+1
    print((rows, cols))

    rr_m = binary_rr(L, rows, cols)
    #print(m)
    nullity = sum(row == [] for row in rr_m)  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1

#print(C(5,10))
#print(C(40,55))
#print(C(1000,1234))
print(C(1000000,1234567))
