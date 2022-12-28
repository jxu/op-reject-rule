# "Streaking" to victory :3
# n = 1 mod 2, 1 mod 3, ..., 1 mod k, n != 1 mod k+1
from number import lcm  # math.lcm is python 3.9+
from functools import reduce

def lcm_n(n):
    return reduce(lcm, range(1, n+1), 1)

def P(s, N):
    return sum(n % (s+1) != 1 for n in range(1, N, lcm_n(s)))

print(sum(P(i, 4**i) for i in range(1, 32)))
