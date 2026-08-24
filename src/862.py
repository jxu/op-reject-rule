# Basic idea: for permutations of digits, e.g. 9 perms [2023, 2032, ...]
# Sum over perms T(p) = 8+7+...+1+0 = 9*(9-1)/2
# Then for each multiset/histogram [c0 0s, ..., c9 9s]
# There are multinomial (N choose c0,...,c9) permutations
# exclude c0 / N perms start with leading 0

# My original solution involved generating partitions of k, like 1+1+2, then
# some string combinatorics based on if the multiset had zeros or not

from math import prod, factorial

# factorial recomputing is really slow 
fact = [factorial(i) for i in range(13)]

# trying out generator to save memory
# also aryanc403 idea: use DP to return sum of c, c^2?
def make_hists(N, min_d=0):
    if N == 0:
        yield [0] * 10
        return

    for d in range(min_d, 10):
        for hist in make_hists(N-1, d):
            hist[d] += 1
            yield hist


def T(N, hist):
    c = (fact[N] // prod(fact[hist[i]] for i in range(10)) *
         (N - hist[0]) // N)
    return c * (c-1) // 2


def S(N):
    return sum(T(N, hist) for hist in make_hists(N))

print(S(12))
