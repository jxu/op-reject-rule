# Use "segment tree" to store info about segments

# For each update of array A, update segments upward in tree:
# u[si] = segment sum
# p[si] = max prefix sum
# s[si] = max suffix sum
# w[si] = max subarray sum within seg

# then for each step, updating associated segtree is O(log(n))

def update_seg(A, j, u, p, s, w):
    n = len(A)
    si = 2 ** (n-1).bit_length() + j

    u[si] = A[j]
    p[si] = A[j]
    s[si] = A[j]
    w[si] = A[j]

    while si > 1:
        l = 2 * (si//2)
        r = l + 1
        u[si//2] = u[l] + u[r]
        p[si//2] = max(p[l], u[l] + p[r])
        s[si//2] = max(s[r], s[l] + u[r])
        w[si//2] = max(w[l], w[r], s[l] + p[r])

        si //= 2


def S(n, l_lo, l_hi):
    A = [0] * n

    u = [0] * 4*n
    p = [0] * 4*n
    s = [0] * 4*n
    w = [0] * 4*n

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
            for m in range(len(A)):
                update_seg(A, m, u, p, s, w)

        else:
            update_seg(A, j, u, p, s, w)

        M = w[1]
        Mtotal += M

    return Mtotal


#print(S(5, 0, 6))
print(S(10**7 + 3, 10**7, 10**7 + 200000))
