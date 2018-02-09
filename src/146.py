# Basic modular arithmetic observations
# n^2 + 1 prime => n even
# n^2 + 3 prime => n not div by 3
# From quadratic residues we have n^2 = 0, 1, 4 mod 5.
# n^2 = 1 mod 5 => 5 | (n^2 + 9) and n^2 = 4 mod 5 => 5 | (n^2 + 1), so
# we must have n^2 = 0 mod 5 => n = 0 mod 5.
# Similarly since n^2 = 0,1,2,4 mod 7, n^2 = 0,1,4 mod 7 are out.
# n^2 = 2 mod 7 => n = 3, 4 mod 7.
# n^2 = 1,3,9 mod 13 => n = 1,3,4,9,10 mod 13

# Combining these congruences we get n = 10, 80, 130, 200 mod 210.
# Python 3: 38s  Pypy 5.1.2: 17s

from number import is_prime

def consecutive_prime(n):
    if any(not is_prime(n**2 + i, 10) for i in (1, 3, 7, 9, 13, 27)):
        return False

    # No need to consider i if multiple of 5
    if any(is_prime(n**2 + i, 10) for i in (11, 17, 19, 21, 23)):
        return False

    return True


def f(n):
    s = 0
    for m in range(0, n+1, 210):
        for k in (m+10, m+80, m+130, m+200):
            if k%13 not in (1, 3, 4, 9, 10): continue
            if consecutive_prime(k):
                print(k)
                s += k
    return s

print(f(150*10**6))