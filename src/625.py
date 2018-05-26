from number import totient_range, totient_sum, sieve, memoize

M = 998244353

@memoize
def totient_sum_memo(n):
    return totient_sum(n)

def G(N):
    s = 0
    for k in range(1, int(N**0.5)+1):
        s = (s + (k*(k+1)//2) * (totient_sum_memo(N//k) - totient_sum_memo(N//(k+1))))
        if k < 100 or k % 100 == 0: print(s, k)

    phi = totient_range(int(N ** 0.5))
    for j in range(1, int(N**0.5)-1):
        s += (N//j)*(N//j + 1) * phi[j] // 2

    return s

print(G(10**2) % M)