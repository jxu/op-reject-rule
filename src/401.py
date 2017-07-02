# (Using OEIS A024916 notation) Sum_{k=1..n} k^2 * floor(n/k)
# Consider case with k <= sqrt(n) and case floor(n/k) <= sqrt(n)
# Observation: for lots of k, floor(n/k) is constant. Let m = n//k,
# sum_{m=1..floor(sqrt(n))} m * (sum_{k=n//(m+1)+1..n//m} k^2)
# Then for k <= sqrt(n), sum the original equation manually (taking care of
# overlap).

from __future__ import division

# Proof of concept. https://math.stackexchange.com/a/2343529
def SIGMA1(n):
    isqrt = int(n**0.5)
    s = 0
    for m in range(1, isqrt+1):
        a = n // (m+1) + 1
        b = n // m
        s += m * (a+b) * (1-a+b) // 2

    for k in range(1, isqrt):
        s += k * (n // k)

    if isqrt != n//isqrt:
        s += isqrt * (n//isqrt)

    return s


def SIGMA2(n):
    isqrt = int(n**0.5)
    s = 0
    for m in range(1, isqrt+1):
        a = n // (m+1)
        b = n // m
        # Inner sum by sum of squares formula
        s += m * (((b*(b+1)*(2*b+1))//6) - ((a*(a+1)*(2*a+1))//6))

    for k in range(1, isqrt+1):
        s += k**2 * (n // k)


    return s % 10**9

print(SIGMA2(10**15))
