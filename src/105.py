# Brute force subsets
# Since removing the union of two sets doesn't change which set sum is greater
# or which has more elements, we can compare all subsets instead of disjoint
# ones
from number import powerset

def is_special(s):
    all_sum = set()
    sum_by_len = [[] for i in range(len(s)+1)]  # List of subsets, indexed by length
    for subset in powerset(s):
        # Check sum of all subsets
        if sum(subset) in all_sum: return False
        all_sum.add(sum(subset))

        sum_by_len[len(subset)].append(sum(subset))

    # Ensure if |B| > |C| then S(B) > S(C)
    for i in range(1, len(sum_by_len)):
        if min(sum_by_len[i]) <= max(sum_by_len[i-1]):
            return False

    return True


with open("p105_sets.txt") as f:
    lines = f.readlines()

special_sum = 0
for line in lines:
    s = sorted(map(int, line.strip().split(',')))
    A = is_special(s)
    print(s, A)
    if A: special_sum += sum(s)

print(special_sum)
