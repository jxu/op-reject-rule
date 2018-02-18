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
