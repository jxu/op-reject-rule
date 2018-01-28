# A subset pair (s1, s2) doesn't need to be checked if every element a in s1
# can be paired 1-to-1 with an element b in s2 such that a > b
# Ex. For a<b<c<d, a<c and b<d => a+c<b+d
# Brute force all subset pairs of equal size and try to pair using backtrack

from itertools import combinations

def certain_inequality(s1, pool, i, l):
    if pool == []:
        return True

    for x in pool:
        new_pool = pool[:]
        new_pool.remove(x)

        if x > s1[i]:
            if certain_inequality(s1, new_pool, i+1, l + [x]):
                return True

    return False


def count_test(n):
    s = 0

    for k in range(2, n//2 + 1):
        subset_pairs = 0
        certain_pairs = 0

        vals = list(range(n))
        for s1 in combinations(vals, k):
            s2_pool = [v for v in vals if v not in s1]
            for s2 in combinations(s2_pool, k):
                subset_pairs += 1
                if certain_inequality(s1, list(s2), 0, []):
                    print(s1, s2)
                    certain_pairs += 1


        s += subset_pairs//2 - certain_pairs

    return s

print(count_test(12))