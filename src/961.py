"""Only matters if digits are 0 or not, so consider all binary
strings of length 18. Each bit represents a non-zero digit (1-9).

In a negamax (simplification of negamax) game tree for a zero-sum game, 
P1 (first player) wins iff P1 can remove a digit and then P2 can force a win.

Thread has closed-form solutions and Sprague-Grundy solutions I didn't
bother figuring out.
"""

from functools import cache

def remove_bit(x, d):
    """Remove dth bit from x, shifting over hi bits"""
    lomask = (1 << d) - 1
    himask =  (~lomask) << 1
    return (x & lomask) | ((x & himask) >> 1)

@cache
def negamax(x):
    """Returns 1 if first player wins starting with x, -1 otherwise"""
    if x == 0: return -1
    for d in range(x.bit_length()):
        if -negamax(remove_bit(x, d)) == 1:
            return 1
    return -1

def w(n):
    return sum((negamax(x) == 1) * (9 ** x.bit_count()) for x in range(2**n))

print(w(18))
