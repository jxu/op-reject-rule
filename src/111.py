# Itertools magic

from number import is_prime
from itertools import combinations_with_replacement as rep_combo

def unique_permutations(elements):
    # Like itertools.permutations but without duplicates. Credit: Luka Rahne

    class unique_element:
        def __init__(self, value, occurrences):
            self.value = value
            self.occurrences = occurrences

    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)


def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

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
