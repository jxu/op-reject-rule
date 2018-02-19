# One of the best PE problems, hands down.
# Key idea: Use limited set of denominators, based on fractions given in 152.m
# For example: if 1/7^2 in sum, some other 1/(7k)^2 must be later in the sum!
# Also use some simple heuristics and integer math.

from __future__ import division
from number import lcm, sieve

D_MAX = 80
primes = sieve(80)

def max_prime_factor(d):
    for p in reversed(primes):
        if d%p == 0: return p

denoms = []
for d in range(2, D_MAX+1):
    # Further analysis with powers of primes (credit: lzw75) excludes these
    # Now runs with PyPy under 1 sec
    if d in (16, 32, 48, 64, 27, 54, 25, 50, 49): continue
    if max_prime_factor(d) <= 7: denoms.append(d)

denoms.extend([13, 39, 52])  # Only set with denom div by 13
denoms = sorted(set(denoms))

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


def f(target, lo, hi, l):
    if target == 0:
        print(l)
        return 1
    if lo > hi or target < 0: return 0
    if numers[hi] > target: return 0
    if tail_sums[lo] < target: return 0


    s = 0
    for denom in denoms:
        if denom < lo: continue
        if denom == 39 and 13 not in l: continue
        if denom == 52 and 39 not in l: continue
        s += f(target - numers[denom], denom+1, hi, l + [denom])

    return s

print(f(lcm_denom//2, 2, D_MAX, []))
