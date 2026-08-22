# Unique groups based on prime base

from functools import cache
from math import gcd
from collections import defaultdict

M = 83456729
n = 34

# primes over N/2 get special repr 1
rad = (
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 1, 
    10, 21, 22, 1, 6, 5, 26, 3, 14, 1,
    30, 1, 2, 33, 34
)

rad_dict = defaultdict(list)
for i in range(2, n+1):
        rad_dict[rad[i]].append(i)

rad_freq = tuple(len(v) for v in rad_dict.values())
rad_repr = tuple(rad_dict.keys())

print("rad dict", rad_dict)
print("rad freq", rad_freq)
print("rad representative", rad_repr)

L = len(rad_freq)

coprime = [[gcd(a, b) == 1 for a in rad_repr] for b in rad_repr]

def extract_count(x, i):
    return (x >> (3*i)) & 7

def subtract_count(x, i):
    return x - (1 << 3*i)

# Pypy int key is much smaller than 3- or 2-tuple
# Memory usage 13.3 GiB -> 3.2 GiB and much faster
def pack(seen, i):
    return (i << 56) | seen

def unpack(key):
    return (key & ((1 << 56) - 1), key >> 56)

@cache
def f(key):
    seen, i = unpack(key)
    if seen == 1 << (3*i): 
        return 1

    length = 0
    for j in range(L):
        length += extract_count(seen, j)

    if length % 2 == rad_repr[i] % 2:
        return 0

    new_seen = subtract_count(seen, i)
    r = 0
    for j in range(L):
        count_j = extract_count(new_seen, j)

        if coprime[i][j] and count_j > 0:
            r = (r +  count_j * f(pack(new_seen, j))) % M

    return r

full = 0
for i in range(L):
    full |= rad_freq[i] << (3*i)

r = 0
for i in range(L):
    r += rad_freq[i] * f(pack(full, i))

print(f.cache_info())
print(r % M)
