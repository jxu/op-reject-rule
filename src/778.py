mod = 1000000009

def digit_mul(a, b):
    """Multiply counts of digits"""
    c = [0] * 10
    for i in range(10):
        for j in range(10):
            c[(i*j)%10] = (c[(i*j)%10] + a[i] * b[j]) % mod
    return c

def F(R, M):
    total = 0
    # calculate each digit place's contribution separately
    for p in range(6):
        # counter for times each digit 0-9 in place 10^p occurs in [0,M]
        c1 = [0] * 10

        # lazy O(M) way instead of combinatorics
        for x in range(M+1):
            c1[(x // (10**p)) % 10] += 1

        c = c1[:]  # result digit counter (for this digit place)

        r = R-1
        while r:  # c^r binary exponentiation for fun
            if r & 1:
                c = digit_mul(c, c1)
            c1 = digit_mul(c1, c1)
            r >>= 1

        # the final answer is just the sum of the answers for each place
        for i in range(10):
            total = (total + i * c[i] * 10**p) % mod

        print(p, c)

    return total


print(F(234567,765432))