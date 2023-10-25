mod = 1000000009

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

        for r in range(1, R):  # can be log(R) with binary exponentiation
            nc = [0] * 10  # temp counter for c
            for i in range(10):
                for j in range(10):
                    # update counter with how many of each digit occurs in
                    # result after a round of multiplication
                    nc[(i*j)%10] = (nc[(i*j)%10] + c[i] * c1[j]) % mod
            c = nc[:]

        # the final answer is just the sum of the answers for each place
        for i in range(10):
            total = (total + i * c[i] * 10**p) % mod

        print(p, c)

    return total


print(F(234567,765432))