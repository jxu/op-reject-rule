"""The main idea comes from prime exponent vectors mod 2
Like from Dixon's / quadratic sieve factorization. 
Seems difficult to come up with the linear algebra on your own.

Let p1, ..., pn be the primes that divide any x in [a,b].
Factor each x = p1^e1 ... pn^en, then represent it as a vector [e1,...,en].
Multiplying x's is adding these vectors mod 2, and zero vector represents a
perfect square.
Let M be the matrix with vector rows for each x in [a,b]. Any linear combo
of rows given by M^T y = 0, so the solution is the 2^dim(left null space)
minus 1 (excluding the empty set).

From here on is sparse Gaussian elimination, because the matrix is too large.

Actually, it turns out this matrix is full rank, so the solution is simply
(b-a+1) - n for computed n.
ecnerwala in the solutions describes why:

For which p does there exist k with k^2 p in [a,b]?
<=> [sqrt(a/p),sqrt(b/p)] contains an integer k.
A sufficient condition is this interval length is >= 1, i.e.
sqrt(b/p) - sqrt(a/p) >= 1, <=> (sqrt(b) - sqrt(a))^2 >= p.
For a = 1000000 and b = 1234567, sqrt(a) = 1000 and sqrt(b) = 1111.1
So just p <= 111.1^2, in particular this holds for p <= sqrt(b).
(But not for [a,b] = [40,55])

So for every p <= sqrt(b), there is some x = k^2 p row that only has a 1
in that p column. Therefore each adds 1 to the rank, and that p can be
eliminated from other rows.

Then for every p > sqrt(b), for any x as a multiple of p, there can be
only one multiple of p, and x/p factors as all primes <= sqrt(b) which are
eliminated out. So these p add 1 to the rank too.

I left the sparse row reduce code anyway because it's more interesting.
"""
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


        if any(primes[pi] > (b-a) for pi in m[i]):
            
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
#print(C(1000000,1234567))
