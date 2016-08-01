# a = 2^x_1 + 3^x_2 + 5^x_3 + 7^x_4 + ...  b = 2^y_1 + 3^y_2 + 5^y_3 + 7^y_4 + ...
# Number of pairs is number of prime exponent pairs 0 <= x_1 <= y_1 <= n, etc.
# Also, (x_1, x_2, ...) != (y_1, y_2, ...) so a and b are distinct
# S((p_m#)^n) = ((n+1)(n+2)/2)^m - (n+1)^m

# Empirical testing shows:  (f(n) means greatest k such that 2^k divides n)
# E(odd m, n = 0 mod 4) = f(n//4) + 1
# E(m, 1 mod 4) = 0
# E(m, 2 mod 4) = 0
# E(m, n = 3 mod 4) = m * (f((n+1)//4)+1)  ex. E(10, 15) = 10 * (f(4)+1) = 30

# Q(n) = sum(f(i)+1, i from 1 to n/4) + sum(904961(f(i)+1), i from 1 to n/4) = 904962 * sum(f(i)+1, i from 1 to n/4)
# Summation function of ruler sequence: A005187 (defined recursively)

# Addendum: empirical testing is actually not needed. A simple analysis by al13n, the first solver, follows from the
# related "factorizations" (n+1)^m (((n+2)/2)^m - 1) and ((n+1)/2)^m ((n+2)^m - 1).
# I noticed a starting point in that the (n+1)(n+2)/2 is even or odd depending on n mod 4, but I wasn't clever enough
# to go from there.
# The problem took me 5 days to solve, and it was on the easy side of number theory...

def E_test(m, n):
    r = ((n+1)*(n+2)//2)**m - (n+1)**m
    E = 0
    while r%2 == 0:
        r //= 2
        E += 1
    print(E, end='\t')
    if n%4 == 3: print()

# Note that Q(8) = 3*m + 3
def small_m_test():
    print('\t', end='')
    for n in range(1, 9):
        E_test(101, n)

# Actual calculations
def special_sum(n):
    if n == 0: return 0
    return special_sum(n//2) + n

def Q(n):
    #assert n % 4 == 0
    return 904962*special_sum(n//4)

print(Q(10**12))