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
# product_combo: 4m 25s, 21898513 work done


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
    vals = [set() for _ in range(n+1)]
    vals[1].add(Fraction(1))
    work = 0

    for i in range(2, n+1):
        for part in partitions(i):
            if len(part) < 2: continue
            for combo in ordered_product_combo(vals, part):
                vals[i].add(sum(combo))  # Parallel
                vals[i].add(1/sum(1/x for x in combo))  # Series
                work += 1

        print(i, work, len(vals[i]))

    return len(set(chain(*vals)))


# It turns out we don't need to partition at all, just use blocks (1, i-1),
# (2, i-2), ... why this works no idea
# 2m 58s with same timing method
def D2(n):
    vals = [set() for _ in range(n+1)]
    vals[1].add(Fraction(1))
    work = 0

    for i in range(2, n+1):
        for j in range(1, i):
            for combo in product(vals[j], vals[i-j]):
                vals[i].add(sum(combo))
                vals[i].add(1/sum(1/x for x in combo))
                work += 1

        print(i, work, len(vals[i]))

    return len(set(chain(*vals)))


print(D2(18))

