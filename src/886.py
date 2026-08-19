# Unique groups based on prime base
# for n = 10
# 2, 4, 8
# 3, 9
# 5
# 6
# 7
# 10

from functools import cache
from math import gcd, prod
from number import factor
from collections import defaultdict
from itertools import accumulate

M = 83456729

# n = 10
#coprime_hist = (3, 2, 1, 1, 1, 1)
#REP          = (2, 3, 5, 6, 7, 10) 

# n = 34
# {2,4,8,16,32}
# {3,9,27}
# {5,25}
# 6, 12, 18, 24
# 10, 20
# 14, 28

def P(n):
    coprime_group = defaultdict(list)

    for i in range(2, n+1):
        rad = prod(factor(i).keys())
        coprime_group[rad].append(i)

    print(coprime_group)

    rad_freq = tuple(len(v) for v in coprime_group.values())
    rad          = tuple(v[0] for v in coprime_group.values())

    print(rad_freq)
    print(rad)

    cp = [[False] * len(rad) for _ in range(len(rad))]

    for i in range(len(rad)):
        for j in range(len(rad)):
            cp[i][j] = gcd(rad[i], rad[j]) == 1

    rad_bitcount = tuple(x.bit_length() for x in rad_freq)

    print("pb_bits", rad_bitcount)

    rad_shift = (0,) + tuple(accumulate(rad_bitcount))[:-1]

    print("shift", rad_shift)

    pb_key = 0
    for i in range(len(rad_freq)):
        pb_key |= (rad_freq[i]) << rad_shift[i]

    print(bin(pb_key))

    def extract_count(bits, i):
        return (bits >> rad_shift[i]) & ((1 << rad_bitcount[i]) - 1)

    def subtract_count(bits, i):
        assert extract_count(bits, i) > 0
        return bits - (1 << rad_shift[i])


    @cache
    def f(seen, i):
        
        #assert seen[i] > 0

        # exactly extract_count(seen, i) == 1 and all other are 0
        if seen == 1 << rad_shift[i]:
            return 1
        
        new_seen = subtract_count(seen, i)

        r = 0
        for j in range(len(rad)):
            count_j = extract_count(seen, j)
            if cp[i][j] and count_j > 0:

                r = (r + count_j * f(new_seen, j)) % M

        #print(seen, i, r)
        return r

    r = 0

    for i in range(len(rad_freq)):
        z = f(pb_key, i)
        print(i, z)
        r = (r + rad_freq[i] * z) % M

    print(f.cache_info())
    return r 

print(P(20))
