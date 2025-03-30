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
But very inefficient with python data structures. Takes about 5 min
"""

from number import linear_sieve

# Row-reduce binary matrix
def binary_rr(L, m, n):
    h = k = 0  # pivot row, col

    while h < m and k < n:
        if k % 1000 == 0: print("pivot", k)
        #print(L)
        piv = None
        for i in range(h, m):
            if k in L[i]:
                piv = i
                break

        if piv == None:
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
    lp = linear_sieve(b)

    rows = b - a + 1
    pfs = [[] for _ in range(rows)]  
    primes = set()  # only primes that divide x in [a,b]
    
    # generage primes list and factorizations
    for x in range(a, b+1):
        y = x
        while y > 1:
            pfs[x-a].append(lp[y])
            primes.add(lp[y])
            y //= lp[y]

    print(pfs)
    primes = sorted(list(primes))
    cols = len(primes)

    # sparse matrix mod 2
    M = [[] for _ in range(rows)]

    for x in range(a, b+1):
        for p in set(pfs[x-a]):
            if pfs[x-a].count(p) % 2:
                # maintaining separate primes_index is a little faster
                M[x-a].append(primes.index(p))

    print(M)
    print("done sparse")
    print(f"matrix {rows} x {cols}")

    rr_m = binary_rr(M, rows, cols)
    #print(m)
    nullity = sum(row == [] for row in rr_m)  # count 0 rows
    print(nullity)
    return pow(2, nullity, 1000000007) - 1

#print(C(5,10))
#print(C(40,55))
#print(C(1000,1234))
print(C(1000000,1234567))
