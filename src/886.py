# Unique groups based on prime base

from functools import cache
from math import gcd
from collections import defaultdict

N = 20
rad_group = defaultdict(list)

rad_lookup = (
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 19, 
    10, 21, 22, 23, 6, 5, 26, 3, 14, 29,
    30, 31, 2, 33, 34
)

for i in range(2, N+1):
    rad_group[rad_lookup[i]].append(i)

print(rad_group)



rad_freq = tuple(len(v) for v in rad_group.values())
rad_repr = tuple(v[0] for v in rad_group.values())


print(rad_freq)
print(rad_repr)

coprime = [[False] * len(rad_repr) for _ in range(len(rad_repr))]

for i in range(len(rad_repr)):
    for j in range(len(rad_repr)):
        coprime[i][j] = gcd(rad_repr[i], rad_repr[j]) == 1

@cache
def f(seen, i):
    assert seen[i] > 0

    if sum(seen) == 1: 
        return 1


    evens = 0
    odds = 0

    for j in range(len(seen)):
        if rad_repr[j] % 2 == 0: 
            evens += seen[j]
        else: 
            odds += seen[j]

    l = sum(seen)

    # n = 10: hits = 253, misses=342
    # with parity: hits = 61, misses = 172

    # n = 20: hits=574131, misses=167527
    # with parity: hits=129379, misses=65429
    

    if l % 2 == 1:
        if not (rad_repr[i] % 2 == 0 and evens - odds == 1): 
            return 0
    else:
        if not (rad_repr[i] % 2 == 1 and evens == odds):

            return 0

    
    new_seen = tuple(seen[k]-1 if k==i else seen[k] 
                for k in range(len(seen)))

    r = 0
    for j in range(len(seen)):
        if coprime[i][j] and seen[j] > 0:

            r += seen[j] * f(new_seen, j)

    return r

def P(n):
    r = 0

    for i in range(len(rad_freq)):
        z = f(rad_freq, i)
        print(i, z)
        r += rad_freq[i] * z

    print(f.cache_info())
    return r 

print(P(10))
