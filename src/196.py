# segmented sieve for rows n-2 to n+2
# sieve primes up to sqrt(row_end(n+2)) then sieve over segment

from number import sieve
from math import ceil

MAX_ROW = 7208785 + 2
MAX_ELEM = MAX_ROW * (MAX_ROW+1) // 2
primes = sieve(int(MAX_ELEM**0.5)+1)

def row_start(n): return n*(n-1)//2 + 1
def row_end(n): return n*(n+1)//2

def neighbors(i, r):
    # Moore neighborhood, including center cell
    # doesn't handle near diagonal values near triangle border:
    # n(n+1)/2 = 1,3,6,10,..., (n-1)(n+2)/2 = 2,5,9,14,...
    s = [i-r+1, i-r+2, i, i+1, i+r, i+r+1]
    if i != row_start(r): # handle on border
        s += [i-r, i-1, i+r-1]
    return s


def S(n):
    seg_start = row_start(n-2)
    seg_end = row_end(n+2)
    print("segment", seg_start, seg_end)
    seg = [0] * (seg_end - seg_start + 1)
    for p in primes:
        # assumes p[0]**2 < seg_start
        for i in range(p*ceil(seg_start/p), seg_end+1, p):
            seg[i-seg_start] = 1

    seg_primes = set()
    seg_triplets = [0] * len(seg)

    for i in range(seg_start, seg_end+1):
        if not seg[i-seg_start]:
            seg_primes.add(i)

    for p in seg_primes:
        rows = [n-1, n, n+1]
        r = None
        for row in rows:
            if row_start(row) <= p <= row_end(row):
                r = row
        if r is None: continue

        prime_nbors = [j for j in neighbors(p,r) if j in seg_primes]
        if len(prime_nbors) >= 3:
            for pn in prime_nbors:
                seg_triplets[pn - seg_start] = True

    s = 0
    for i in range(row_start(n), row_end(n)+1):
        if seg_triplets[i - seg_start]: s += i

    return s


print(S(5678027) + S(7208785))
