# First problem solved using squareroot decomposition
# (Pisano period doesn't help)

# For each update of array A, update square-root size segment and
# associated values:
# u[si] = segment sum
# p[si] = max prefix sum
# s[si] = max suffix sum
# w[si] = max subarray sum within seg

# then for each step, updating associated seg values is O(sqrt(n)) and
# M(i) is a DP solution similar to standard max subarray sum problem

from math import ceil
from itertools import accumulate

def max_prefix_sum(seg):
    return max(accumulate(seg))

def max_suffix_sum(seg):
    return max_prefix_sum(reversed(seg))

def max_subsum(seg):
    # Regular Kadane's algorithm
    best = s = 0
    for x in seg:
        s = max(0, s + x)
        best = max(best, s)

    return best

def update_seg(A, seglen, si, u, p, s, w):
    seg = A[si * seglen: (si + 1) * seglen]

    u[si] = sum(seg)
    p[si] = max_prefix_sum(seg)
    s[si] = max_suffix_sum(seg)
    w[si] = max_subsum(seg)


def S(n, l_lo, l_hi):
    A = [0] * n

    seglen = int(n**0.5)
    nseg = ceil(n / seglen)
    u = [0] * nseg
    p = [0] * nseg
    s = [0] * nseg
    w = [0] * nseg

    # pre-compute Tribonacci numbers mod n
    t = [0] * 2*l_hi
    t[2] = 1
    for k in range(3, 2*l_hi):
        t[k] = (t[k-1] + t[k-2] + t[k-3]) % n

    Mtotal = 0

    for i in range(1, l_hi+1):
        # perform array update
        j = t[2*i-2]
        A[j] += 2*t[2*i-1] - n + 1

        if i <= l_lo: continue

        # init seg associated values
        if i == l_lo+1:
            for si in range(nseg):
                update_seg(A, seglen, si, u, p, s, w)

        si = j // seglen  # segment index
        update_seg(A, seglen, si, u, p, s, w)

        M = 0
        msum = 0
        # custom Kadane's algorithm for segments
        for si in range(nseg):
            # Either start segment here or continue last segment
            msum = max(s[si], msum + u[si])
            # include prefix of next segment
            msump = msum + (p[si+1] if si+1 < nseg else 0)
            M = max(M, msump)

        M = max(M, max(w))
        #print(u, p, s, w)
        #print(i, M)
        Mtotal += M

    return Mtotal


#print(S(5, 0, 6))
print(S(10**7 + 3, 10**7, 10**7 + 200000))
