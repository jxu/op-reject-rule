# Let V_n be a possible value made from n capacitors.
# V_n are generated from values of circuits with fewer capcitors:
# V_n = V_m1, ... V_mk, with m1 + ... + mk = n.
# For example, V_3 could be V_1 + V_1 + V_1 or V_1 + V_2 or 1/(1/V_1 + 1/V_2)).
# So for each n from 2 to 18 we generate every possible V_n using V_m values.
# This is done by partitioning n into m1,...,mk and then trying the cartesian
# product of all V_m1 to V_mk by applying the parallel or series formula.\

# Improvements: Cartesian product is wasteful. For example if we use parallel
# V_4 = V_2 + V_2 then we tried 1/2 + 2 and 2 + 1/2. Series formula is
# symmetric too.
# Also for summing, V_1 + V_1 + V_1 is covered by V_2 + V_1.
# Not sure about simplifying series formula.

# Timing: Thinkpad laptop, pypy 5.10.0
# product_combo: 4m 25s
''' Work done (starting at i=2)
1
3
11
28
92
241
731
1996
5886
16062
47046
128199
367782
1008049
2854769
7768320
21898513
'''


from fractions import Fraction
from itertools import product, chain, combinations_with_replacement
from collections import Counter

def partitions(n, I=1):  # Credit: skovorodkin
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p


def product_combo(vals, part):
    blocks = [vals[ind] for ind in part]
    return product(*blocks)

def ordered_product_combo(vals, part):
    cnt = Counter()
    for ind in part: cnt[ind] += 1
    blocks = [combinations_with_replacement(vals[i], cnt[i]) for i in cnt]
    return [list(chain(*combo)) for combo in product(*blocks)]




def D(n):
    vals = [set() for i in range(n+1)]
    vals[1].add(Fraction(1))

    for i in range(2, n+1):
        work = 0
        for part in partitions(i):
            if len(part) < 2: continue
            for combo in ordered_product_combo(vals, part):
                vals[i].add(sum(combo))  # Parallel
                vals[i].add(1/sum(1/x for x in combo))  # Series
                work += 1

        print(i, work, len(vals[i]))
        #print(work)

    return len(set(chain(*vals)))


#vals = [0, (1,), (1, 2, 3)]
#print(list(ordered_product_combo(vals, (1, 2, 2))))
print(D(18))

