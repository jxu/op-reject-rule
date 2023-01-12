from number import combination as comb
M = 10**16
def S(n):
    s = 0
    for d in range(1, 10):
        digit_total = (n * comb(d+n-2, n-2) - comb(n,2)) * 2*d // n
        s += (digit_total % M) * (10**n - 1) // 9

    return s % M


print(S(2020))