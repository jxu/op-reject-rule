from fractions import gcd
s = 0
for d in range(12001):
    for n in range(int(d/3)+1, int(d/2)+1):
        if 2*n != d and gcd(n, d) == 1:
            s += 1

print(s)

def totient_sum(N):
    """Find the sum of phi(n) for 1 to N.

    O(log n) space, O(n^(3/4)) time
    Modified from PE 73 overview. Credit: daniel.is.fischer
    See benchmarks file
    """

    if N < 3:
        return (0, 1, 2)[N]

    K = int((N/2)**0.5)
    M = N // (2*K+1)
    rsmall = [0]*(M+1)
    rlarge = [0]*K

    def F(n):
        return n*(n-1)//2

    def R(n):
        switch = int((n/2)**0.5)
        count = F(n) - F(n//2)
        m = 1
        k = n//2
        while k >= switch:
            nextk = (n // (m+1) - 1) // 2
            count -= (k - nextk)*rsmall[m]
            k = nextk
            m += 1

        while k > 0:
            m = n // (2*k+1)
            if m <= M:
                count -= rsmall[m]
            else:
                count -= rlarge[((N//m) - 1) // 2]
            k -= 1

        if n <= M:
            rsmall[n] = count
        else:
            rlarge[((N//n) - 1) // 2] = count


    for n in range(1, M+1):
        R(n)

    for j in range(K-1, -1, -1):
        R(N // (2*j + 1))

    return rlarge[0] + 1