# Itertools magic

from number import unique_permutations, is_prime
from itertools import combinations_with_replacement as rep_combo

def S(n, d):
    s = 0
    found_M = False
    M = n
    other_digits = [r for r in range(10) if r != d]

    while not found_M:
        for non_rep in rep_combo(other_digits, n-M):
            digits = non_rep + (d,)*M
            for perm in unique_permutations(digits):
                if perm[0] == 0: continue  # Skip nums with leading 0s
                p = 0
                for x in perm: p = 10*p + x

                if is_prime(p):
                    print(p)
                    s += p
                    found_M = True

        M -= 1

    return s

print(sum(S(10, d) for d in range(10)))
