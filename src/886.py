# Unique groups based on prime base
# for n = 10
# 2, 4, 8
# 3, 9
# 5
# 6
# 7
# 10

from functools import cache
from math import gcd
from number import factor
from collections import defaultdict

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

N = 20
coprime_group = defaultdict(list)

for i in range(2, N+1):
    pf = tuple(factor(i).keys())
    coprime_group[pf].append(i)

print(coprime_group)



coprime_hist = tuple(len(v) for v in coprime_group.values())
REP          = tuple(v[0] for v in coprime_group.values())

print(coprime_hist)
print(REP)

cp = [[False] * len(REP) for _ in range(len(REP))]

for i in range(len(REP)):
    for j in range(len(REP)):
        cp[i][j] = gcd(REP[i], REP[j]) == 1

@cache
def f(seen, i):
    
    assert seen[i] > 0

    if sum(seen) == 1: 
        return seen[i] == 1
    
    new_seen = tuple(seen[k]-1 if k==i else seen[k] 
                for k in range(len(seen)))

    r = 0
    for j in range(len(seen)):
        if cp[i][j] and seen[j] > 0:

            r += seen[j] * f(new_seen, j)

    #print(seen, i, r)
    return r

def P(n):
    r = 0

    for i in range(len(coprime_hist)):
        z = f(coprime_hist, i)
        print(i, z)
        r += coprime_hist[i] * z

    return r 

print(P(10))
