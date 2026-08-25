# Basic idea: for permutations of digits, e.g. 9 perms [2023, 2032, ...]
# Sum over perms T(p) = 8+7+...+1+0 = 9*(9-1)/2
# Then for each multiset/histogram [c0 0s, ..., c9 9s]
# There are multinomial (N choose c0,...,c9) permutations
# exclude c0 / N perms start with leading 0

# My original solution involved generating partitions of k, like 1+1+2, then
# some string combinatorics based on if the multiset had zeros or not
from itertools import combinations
from number import multinomial

def weak_compositions(n, m):
    """Generate m-tuples of nonnegative integers that sum to n.
    
    i.e. (a_1, ..., a_m) where a_1 + ... + a_m = n, a_i >= 0.
    """
    # Stars-and-bars approach: pick m - 1 dividers from m + n - 1 slots
    for bars in combinations(range(1, n + m), m - 1):
        bars = (0,) + bars + (n + m,)  # endpoints
        yield tuple(bars[i+1] - bars[i] - 1 for i in range(m))


def S(k):
    def T(comp):
        c = multinomial(comp) * (k - comp[0]) // k
        return c * (c-1) // 2

    return sum(T(comp) for comp in weak_compositions(k, 10))

print(S(12))
