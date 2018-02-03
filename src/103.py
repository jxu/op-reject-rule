# Brute force!!

from number import powerset

# From #105
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

# Guesstimate limits for A_MAX, a
A_MAX = 50
min_sum = 1000
min_s = None
# Oh boy...
for a in range(20, 24):
    for b in range(a+1, A_MAX):
        for c in range(b+1, A_MAX):
            for d in range(c+1, A_MAX):
                for e in range(d+1, A_MAX):
                    for f in range(e+1, A_MAX):
                        # Using e+f+g < a+b+c+d
                        for g in range(f+1, min(A_MAX, a+b+c+d-e-f)):
                            s = [a, b, c, d, e, f, g]
                            if is_special(s):
                                print(s, sum(s))
                                if sum(s) < min_sum:
                                    min_sum = sum(s)
                                    min_s = s

print(''.join(map(str, min_s)))