# brute force: assume base 12 digits only appear once
# 129s with pypy
from number import int_to_base
from itertools import permutations

def pandigital(n, b):
    """Checks if n contains all digits from 0 to b-1"""
    digit_list = int_to_base(n, b)
    return set(digit_list) == set(range(b))


def n_super_pandigital(b):
    s = 0
    found = 0

    digits = list(range(b))
    for permutation in permutations(digits):
        if permutation[0] == 0:
            continue
        # Create num from digit permutation
        n = 0
        base_pow = 1
        for digit in reversed(permutation):
            n += digit * base_pow
            base_pow *= b

        valid = True
        for test_base in range(b-1, 1, -1):
            if not pandigital(n, test_base):
                valid = False
                break

        if valid:
            print(permutation, n)
            s += n
            found += 1

        if found == 10:
            return s


print(n_super_pandigital(12))
