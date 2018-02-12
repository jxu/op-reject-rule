from __future__ import division
from number import memoize
from fractions import Fraction

x = 0

D_MAX = 80
tail_sum = [0]*(D_MAX+1)
tail_sum[D_MAX] = 1/(D_MAX**2)
for i in range(D_MAX, 1, -1):
    tail_sum[i] = tail_sum[i+1] + 1/(i**2)


@memoize
def f(target, lo, hi):
    if lo > hi or target < 0: return 0
    if float(target) - 1/(hi**2) < 0: return 0
    if tail_sum[lo] < target: return 0

    if target == 0:
        return 1

    global x
    x += 1

    s = 0
    for denom in range(lo, hi+1):
        s += f(target - Fraction(1, denom**2), denom+1, hi)

    return s

print(f(Fraction(1, 2), 2, 20))
print(x)



