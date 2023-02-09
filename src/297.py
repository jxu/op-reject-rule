# A007895: z(n)
# A179180: Z(n) but 1-indexed

from number import fib_list, memoize
from bisect import bisect_left
fib = fib_list(90)

@memoize
def Z(N):
    if N < 2: return 0
    i = bisect_left(fib, N) - 1
    return N - fib[i] + Z(N - fib[i]) + Z(fib[i])

print(Z(10**17))