from __future__ import division
from number import memoize, lcm, is_prime

tests = 0
D_MAX = 35

# prime test
denoms = [d for d in range(2, D_MAX+1) if d <= D_MAX/2 or not is_prime(d)]

lcm_denom = 1
for d in denoms:
    lcm_denom = lcm(lcm_denom, d**2)

print(denoms, lcm_denom)

numers = [0]*(D_MAX+1)
for d in denoms:
    numers[d] = lcm_denom // (d**2)

tail_sums = [0]*(D_MAX+1)
tail_sums[D_MAX] = numers[D_MAX]
for i in range(D_MAX-1, 1, -1):
    tail_sums[i] = tail_sums[i+1] + numers[i]

print(numers)


#@memoize
def f(target, lo, hi):
    if target == 0: return 1
    if lo > hi or target < 0: return 0
    if numers[hi] > target: return 0
    if tail_sums[lo] < target: return 0


    global tests
    tests += 1

    s = 0
    for denom in denoms:
        if denom < lo: continue
        s += f(target - numers[denom], denom+1, hi)

    return s

print(f(lcm_denom//2, 2, D_MAX))
print(tests)
print(sum(numers[i] for i in (2,3,4,5,7,12,15,20,28,35)), lcm_denom//2)