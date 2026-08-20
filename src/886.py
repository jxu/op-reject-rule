# Unique groups based on prime base

from functools import cache
from math import gcd
from collections import defaultdict
from number import is_prime

M = 83456729
N = 10
rad_group = defaultdict(list)

rad_lookup = (
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 19, 
    10, 21, 22, 23, 6, 5, 26, 3, 14, 29,
    30, 31, 2, 33, 34
)

for i in range(2, N+1):
    # optimization: wildcard primes grouped together
    if i > N // 2 and is_prime(i):
        # 1 coprime to everything?
        rad_group[1].append(i)
    else:
        rad_group[rad_lookup[i]].append(i)

print(rad_group)



rad_freq = tuple(len(v) for v in rad_group.values())
rad_repr = tuple(rad_group.keys())


print("rad freq", rad_freq)
print("rad representative", rad_repr)

coprime = [[False] * len(rad_repr) for _ in range(len(rad_repr))]

for i in range(len(rad_repr)):
    for j in range(len(rad_repr)):
        coprime[i][j] = gcd(rad_repr[i], rad_repr[j]) == 1


# lazy bitpacking
def extract_bits(x, i):
    return (x >> (3*i)) & 7

def subtract_count(x, i):
    return x - (1 << 3*i)

@cache
def f(seen, i):


    if seen == (1 << (3*i)): 
        return 1

    new_seen = subtract_count(seen, i)

    r = 0
    for j in range(len(rad_freq)):
        count_j = extract_bits(new_seen, j)

        if (coprime[i][j]) and count_j > 0:

            r = (r +  count_j * f(new_seen, j)) % M

    return r

full = 0
for i in range(len(rad_freq)):
    full |= rad_freq[i] << (3*i)

r = 0

for i in range(len(rad_freq)):
    z = f(full, i)
    print(i, z)
    r += rad_freq[i] * z

print(f.cache_info())
print(r % M)

