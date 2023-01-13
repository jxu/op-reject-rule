# DS-number has n-1 digits that sum to d, then digit d somewhere
# How many n-length DS-numbers sum to 2d?
# By stars-and-bars, placing n-1 digits that sum to d is (d+n-2 choose n-2)
# then n places to put digit d, but subtract (n choose 2) because cases with
# two digit d's (like 3300) are overcounted once.

# Then every DS-number sums to 2d and each digit is treated symmetrically vs
# all others, so adding up all DS-numbers digit by digit,
# each digit gets on average (2d / n) * (# DS-numbers)
# Adding up these numbers digit by digit is the same as multiplying the digit
# avg by 111... (= (10^n-1)/9)

from number import comb
M = 10**16
def S(n):
    s = 0
    for d in range(1, 10):
        digit_total = (n * comb(d+n-2, n-2) - comb(n,2)) * 2*d // n
        s += (digit_total % M) * (10**n - 1) // 9

    return s % M


print(S(2020))