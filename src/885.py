# Uninteresting brute force on possible ascending digit nums
# See solution thread for constant-time solution!
from math import factorial
M = 1123455689

def g(max_d, digits_left):
    if not digits_left:
        yield 0; return

    for d in range(max_d+1):
        for s in g(d, digits_left-1):
            yield 10*s + d  # build right-to-left. faster than string ops


def S(n):
    # runs just as fast without using mod arithmetic
    fact = [factorial(i) for i in range(n+1)]

    r = 0
    for m in g(9, n):
        z = m
        digit_counts = [0]*10
        for i in range(n):  # for leading zeros, add to 0 count
            digit_counts[z%10] += 1
            z //= 10

        t = fact[n]
        for d in range(10):
            t //= fact[digit_counts[d]]
        r += m*t

    return r

print(S(18) % M)