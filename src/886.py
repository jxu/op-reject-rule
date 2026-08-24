"""Coprime Permutations

Surprisingly optimizable problem with a simple statement.
The permutation can be viewed as a Hamiltonian path on a graph with numbered
vertices and edges for coprime pairs, although I don't think this helps.

The standard approach is DP, keeping track of a seen (visited) set of nodes
and the current end node. Recurse through paths through the seen set.
(Apparently similar to the Held-Karp algorithm for a related TSP problem.)

The problem with this is the state space is O(2^n * n), and each state
requires O(n) calculations. For n = 33, this is too large, but still close
to feasible.

The key observation (found after looking through some values) is coprimality
between two numbers only depends on their prime factors and not multiplicity.
So numbers can be grouped by their "prime bases", or more compactly radical,
the product of the distinct prime factors. Instead of a binary visited set,
now keep track of counts. This reduces 33 integers to 21 classes.

{2, 4, 8, 32}
{3, 9, 27}
{5, 25}
{6, 12, 18, 24}
{7}
{10, 20}
{11}
{13}
{14, 28}
{15} {17} {19} {21} {22} {23} {26} {29} {30} {31} {33} {34}

This still runs too slow, even with pypy bitsets, and even rewritten in C++. 

Another observation I made early on is that primes > n/2 are coprime to all,
so they can be treated as their own special class which is also coprime to
its own members. Conveniently, I noticed rad 1 could be used for this, as it's
coprime even to itself. This combines {19, 23, 29, 31} into its own class,
leaving 18 classes.
This was finally enough to get the C++ rewrite to run in a few minutes.

Another optimization I included, actually my first approach, is to notice all
paths are the form even-odd-even-odd-...-even. 
(Note this only works for even n.)
The recursion uses path prefixes, so I can enforce even/odd constraint on the
end node based on path length. I also considered things like #even - #odd = 1
which is redundant. This cuts down on the original DP states by something like
O(1 / sqrt n) since it compares O(2^n) to O((n choose n/2)).
"""

from math import gcd
from collections import defaultdict

M = 83456729
n = 34

# primes over N/2 get special rad 1
rad = (
    0, 0, 2, 3, 2, 5, 6, 7, 2, 3, 
    10, 11, 6, 13, 14, 15, 2, 17, 6, 1, 
    10, 21, 22, 1, 6, 5, 26, 3, 14, 1,
    30, 1, 2, 33, 34
)

# manually maintain memo for more control than @cache
memo = {}

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

# Pack rad counts into packed binary int
def extract_count(x, i):
    return (x >> (3*i)) & 7

def subtract_count(x, i):
    # assumes count >= 1
    return x - (1 << 3*i)

# Pypy int key is much smaller than 3- or 2-tuple
# Memory usage of @cache 13.3 GiB -> 3.2 GiB and much faster
def pack(seen, i):
    return (i << 56) | seen

def f(seen, i, height):
    key = pack(seen, i)
    if key in memo:
        return memo[key]

    if seen == 1 << (3*i):  # base case
        return 1

    # even-odd optimization
    if height % 2 == rad_repr[i] % 2:
        return 0

    new_seen = subtract_count(seen, i)
    r = 0
    for j in range(L):
        count_j = extract_count(new_seen, j)

        if coprime[i][j] and count_j > 0:
            r = (r +  count_j * f(new_seen, j, height-1)) % M

    memo[key] = r
    return r

# load max rad_freq into packed binary
full = 0
for i in range(L):
    full |= rad_freq[i] << (3*i)

# sum main DP over all ending nodes
r = 0
for i in range(L):
    r += rad_freq[i] * f(full, i, n-1)

print(r % M)
