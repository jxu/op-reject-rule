# DP with one parameter solution basically by Reiner Martin
# Examine first value i of twopal.
# If i != 2, remove first and last value from smaller twopal.
# If i = 2, then inner palindrome sums to n-4, and there are 2^((n-4)//2)
# such palindromes.
# This gives the recurrence
# t(n) = 2^{(n-4)//2} + t(n-2) + sum_{i=3..n/2} t(n-2i)
# = sum_{i=0..n/2-1} t(2i) - t(n-4) + 2^{(n-4)//2}

# Defining partial sums s(n) = sum_{i=0..n/2} t(2i) we get the recurrences
# t(n) = s(n-2) - t(n-4) + 2^((n-4)//2)
# s(n) = s(n-2) + t(n)

from functools import lru_cache
M = 1000000

@lru_cache()
def s(n):
    if n < 2: return 0
    return (s(n-2) + t(n)) % M

@lru_cache()
def t(n):
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 0
    return (s(n-2) - t(n-4) + pow(2, (n-4)//2, M)) % M

for n in range(43, 10**7):
    if t(n) == 0:
        print(n)
        break


