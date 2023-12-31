# The Zeckendorf representation of $a$ can be computed greedily:
# for$F_n < a < F_{n+1$, let F_n be part of the representation,
# and leftover a - F_n < F_{n+1} - F_n = F_{n-1}.
#
# This inspires the sum (for F_n as large as possible such that F_n < N)
# \sum_{a=F_n}^{N-1} z(a) = (N - F_n) + \sum_{a=0}^{N-1-F_n} z(a)
#
# Letting partial sums function (up to but excluding n)
# Z(n) = \sum_{i=0}^{n-1} z(i), the sum is equivalent to
# Z(N) - Z(F_n) = (N - F_n) + Z(N - F_n)
# The final recurrence is then
# Z(N) = (N - F_n) + Z(N - F_n) + Z(F_n)
#
# This is a recurrence in terms of two Z terms, but Z(F_n)'s can be
# precomputed with N = F_{n+1}:
# Z(F_{n+1}) = F_{n-1} + Z(F_n) + Z(F_{n-1})

# A007895: z(n)
# A179180: Z(n) shifted

from functools import cache
from number import fib_list
from bisect import bisect_left
fib = fib_list(90)

@cache
def Z(N):
    if N < 2: return 0
    i = bisect_left(fib, N) - 1  # rightmost value less than N
    return N - fib[i] + Z(N - fib[i]) + Z(fib[i])

print(Z(10**17))