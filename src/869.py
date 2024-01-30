# Thought about using suffix tree / trie in Python, but ended up keeping track
# of suffixes indexed by bit value and bit length.
# The extra Bitstring dataclass I wrote wasn't necessary

# Let E(...x) = the expected score given known bitstring x.
# For example, given known bits ...x, the expected score guessing 0 by cases:
# Actual string ...0x with prob P(...0x); expected score is 1 + E(...0x)
# Actual string ...1x with prob P(...1x); expected score is E(...1x)
# Actual string was exactly x with prob P(x); guess was extraneous

# Then we can write a recursive formula for guessing
# guess 0: g0 = P(...0x)*(1 + E(...0x)) + P(...1x)*E(...1x)
# guess 1: g1 = P(...1x)*(1 + E(...1x)) + P(...0x)*E(...0x)
# E(...x) = max(g0, g1)

from number import sieve
from collections import Counter

N = 10**8
B = N.bit_length()
suf = [Counter() for _ in range(B+1)]
primes = sieve(N)

for p in primes:
    # add p's suffixes to Counters
    for i in range(p.bit_length()+1):
        mask = (1 << i) - 1
        suf[i][p & mask] += 1

def E(x : int, b : int) -> float:
    if b == B: return 0
    total = suf[b][x]
    if total == 0: return 0

    x0 = x  # append 0 msb
    x1 = x | (1 << b)  # append 1 msb

    p0m, p1m = suf[b+1][x0], suf[b+1][x1]
    e0, e1 = E(x0, b+1), E(x1, b+1)
    g0 = p0m * (1 + e0) + p1m * e1
    g1 = p1m * (1 + e1) + p0m * e0

    return max(g0, g1) / total


print(round(E(0, 0), 8))