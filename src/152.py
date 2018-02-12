from __future__ import division
from number import memoize, lcm
#from fractions import Fraction

x = 0

D_MAX = 45
lcm_denom = 1
for i in range(2, D_MAX+1):
    lcm_denom = lcm(lcm_denom, i**2)

print(lcm_denom)

numers = [0]*(D_MAX+1)
for i in range(2, D_MAX+1):
    numers[i] = lcm_denom // (i**2)

tail_sums = [0]*(D_MAX+1)
tail_sums[D_MAX] = numers[D_MAX]
for i in range(D_MAX-1, 1, -1):
    tail_sums[i] = tail_sums[i+1] + numers[i]


@memoize
def f(target, lo, hi):
    if lo > hi or target < 0: return 0
    if numers[hi] > target: return 0
    if tail_sums[lo] < target: return 0

    if target == 0:
        return 1


    global x
    x += 1

    s = 0
    for denom in range(lo, hi+1):
        s += f(target - numers[denom], denom+1, hi)

    return s

print(f(lcm_denom//2, 2, 20))
print(x)
