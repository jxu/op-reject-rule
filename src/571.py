from number import int_to_base
from itertools import permutations

def pandigital(n, b):
    """Checks if n contains all digits from 0 to b-1"""
    digit_list = int_to_base(n, b)
    return set(digit_list) == set(range(b))


def n_super_pandigital(b):
    l = []
    for extra_digit in range(b):
        #digits = list(range(b)) + [extra_digit]
        digits = range(b)
        for permutation in permutations(digits):
            print(permutation)
            # Create num from digit permutation
            n = 0
            base = 1
            for digit in reversed(permutation):
                n += digit * base
                base *= b

            valid = True
            for test_base in range(b-1, 1, -1):
                if not pandigital(n, test_base):
                    valid = False
                    break

            if valid:
                print(n)
                l.append(n)

            if len(l) == 10:
                return l


n_super_pandigital(12)