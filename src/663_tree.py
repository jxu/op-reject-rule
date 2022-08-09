# Use "segment tree" to store info about segments


# For each update of array A, update segments upward in tree:
# u[si] = segment sum
# p[si] = max prefix sum
# s[si] = max suffix sum
# w[si] = max subarray sum within seg

# then for each step, updating associated segtree is O(log(n))


def update_seg(A, seglen, si, u, p, s, w):
    


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
