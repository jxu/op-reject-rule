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

    coprime_hist = tuple(len(v) for v in coprime_group.values())
    REP          = tuple(v[0] for v in coprime_group.values())

    print(coprime_hist)
    print(REP)

    cp = [[False] * len(REP) for _ in range(len(REP))]

    for i in range(len(REP)):
        for j in range(len(REP)):
            cp[i][j] = gcd(REP[i], REP[j]) == 1

    pb_bits = tuple(x.bit_length() for x in coprime_hist)

    print("pb_bits", pb_bits)

    pb_shift = (0,) + tuple(accumulate(pb_bits))[:-1]

    print("shift", pb_shift)

    pb_key = 0
    for i in range(len(coprime_hist)):
        pb_key |= (coprime_hist[i]) << pb_shift[i]

    print(bin(pb_key))

    def extract_count(bits, i):
        return (bits >> pb_shift[i]) & ((1 << pb_bits[i]) - 1)

    def subtract_count(bits, i):
        assert extract_count(bits, i) > 0
        return bits - (1 << pb_shift[i])


    @cache
    def f(seen, i):
        
        #assert seen[i] > 0

        # exactly extract_count(seen, i) == 1 and all other are 0
        if seen == 1 << pb_shift[i]:
            return 1
        
        new_seen = subtract_count(seen, i)

        r = 0
        for j in range(len(REP)):
            if cp[i][j] and extract_count(seen, j) > 0:

                r += extract_count(seen, j) * f(new_seen, j)

        #print(seen, i, r)
        return r

    r = 0

    for i in range(len(coprime_hist)):
        z = f(pb_key, i)
        print(i, z)
        r += coprime_hist[i] * z

    print(f.cache_info())
    return r 

print(P(20))
