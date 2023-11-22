# Basic idea: for permutations of digits, ex. 9 perms for 2023, 2032, ...
# Contribution to S(N) is 8+7+...+1+0
# Rest is slightly involved string combinatorics.
# I generated partitions without assigning digits first, but using histograms
# of digits is easier and still tractable.

from math import factorial
from number import prod
from collections import Counter

def partition(n, m=1):
    """Partition n into ordered parts

    :param n: integer to partition
    :param m: min new value to add (for recursion)
    :return: list of ordered parts, e.g. [[1,1,1], [1,2], [3]]
    """
    if n == 0: return [[]]
    r = []
    for i in range(m, n+1):
        for l in partition(n-i, i):
            r.append([i] + l)

    return r


def S(k):
    s = 0
    for part in partition(k):
        l = len(part)
        counter = Counter(part)
        # string permutations, e.g. aabc
        c = factorial(k) // prod(factorial(x) for x in part)

        #digit assignments without 0
        j = prod(range(9,9-l,-1)) // prod(map(factorial, counter.values()))

        s += j * c * (c-1) // 2  # contribution to S

        # digit assignments with 0: assign 0 to letters appearing
        # once, twice, etc.
        for x in counter.keys():
            counter[x] -= 1
            j = (prod(range(9, 9-(l-1), -1)) //
                 prod(map(factorial, counter.values())))

            c0 = c * (k - x) // k  # prop not starting with 0
            s += j * (c0-1)*c0 // 2

            counter[x] += 1  # restore

    return s


print(S(12))
