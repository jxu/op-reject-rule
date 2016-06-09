# Dynamic programming
# Recursive relation f(n, pow2) = f(n, pow2/2) + f(n - pow2, pow2/2) + f(n - 2*pow2, pow2/2)
from math import log

memo = {}
def f(n, pow2):
    if n < 0: return 0
    if pow2 == 0: return 1 if n == 0 else 0
    if (n, pow2) in memo: return memo[(n, pow2)]

    # Max sum with pow2 is 2*(pow2 + pow2/2 + pow2/4 + ...) = 2*(2*pow2 - 1)
    # No need to memoize
    if n > 2*(2*pow2 - 1): return 0

    s = f(n, pow2//2) + f(n - pow2, pow2//2) + f(n - 2*pow2, pow2//2)
    memo[(n, pow2)] = s
    return s

n = 10**25
print(f(n, 2**int(log(n, 2))))
print(memo)