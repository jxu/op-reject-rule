from number import pandigital
from itertools import permutations

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