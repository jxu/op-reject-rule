# First problem solved using squareroot decomposition
# (Pisano period doesn't help)

# For each update of array A, update square-root size segment and
# associated values:
# u[si] = segment sum
# s[si] = max subarray sum using seg start value (or empty)
# e[si] = max subarray sum using seg end value (or empty)
# w[si] = max subarray sum within seg

# then for each step, updating associated seg values is O(sqrt(n)) and
# M(i) is a DP solution similar to standard max subarray sum problem

from math import ceil

def max_start_sum(seg):
    best = s = 0
    for x in seg:
        s += x
        best = max(best, s)

    return best

def max_end_sum(seg):
    return max_start_sum(reversed(seg))

def max_subsum(seg):
    # Regular Kadane's algorithm
    best = s = 0
    for x in seg:
        s = max(0, s + x)
        best = max(best, s)

    return best


def S(n, l_lo, l_hi):
    A = [0] * n

    seglen = int(n**0.5)
    nseg = ceil(n / seglen)
    u = [0] * nseg
    s = [0] * nseg
    e = [0] * nseg
    w = [0] * nseg

    # pre-compute Tribonacci numbers
    t = [0] * 2*l_hi
    t[2] = 1
    for k in range(3, 2*l_hi):
        t[k] = (t[k-1] + t[k-2] + t[k-3]) % n

    Mtotal = 0

    for i in range(1, l_hi+1):
        # perform array update
        j = t[2*i-2] % n
        A[j] += 2*(t[2*i-1] % n) - n + 1

        if i <= l_lo: continue

        # init seg associated values
        if i == l_lo+1:
            for si in range(nseg):
                seg = A[si*seglen : (si+1)*seglen]

                u[si] = sum(seg)
                s[si] = max_start_sum(seg)
                e[si] = max_end_sum(seg)
                w[si] = max_subsum(seg)

        si = j // seglen  # segment index
        seg = A[si*seglen : (si+1)*seglen]

        u[si] = sum(seg)
        s[si] = max_start_sum(seg)
        e[si] = max_end_sum(seg)
        w[si] = max_subsum(seg)

        M = 0
        msum = 0
        # custom Kadane's algorithm for segments
        for k in range(nseg):
            # Either start segment here or continue last segment
            msum = max(e[k], msum + u[k])

            msume = msum
            if k+1 < nseg: msume += s[k+1]
            M = max(M, msume)

        M = max(M, max(w))
        #print(M)
        Mtotal += M

    return Mtotal


print(S(10**7 + 3, 10**7, 10**7 + 200000))
