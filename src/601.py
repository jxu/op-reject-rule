# "Streaking" to victory :3
# n = 1 mod 2, 1 mod 3, ..., 1 mod k, n != 1 mod k+1
# math.lcm is python 3.9+
from number import lcm
from functools import reduce

def lcm_n(n):
    return reduce(lcm, range(1, n+1), 1)

def P(s, N):
    count = 0
    for n in range(1, N, lcm_n(s)):
        if n % (s+1) != 1: count += 1
    return count


s = 0
for i in range(1, 32):
    s += P(i, 4**i)
print(s)