# Subset sum problem variation
# linear 2-sum on all pairs f_n(a) + f_n(b), f_n(c) + f_n(d)
from math import pi, log, exp, isclose

def g(n):
    k_max = int(n * log(pi+1))  # all fn(k) non-negative
    fn = [exp(k/n) - 1 for k in range(k_max)]
    print(k_max)

    # python tuples take a lot of memory, so just store pair sum and
    # recover a, b afterwards
    pairs = sorted([fn[a] + fn[b] for a in range(k_max)
                   for b in range(a, k_max)])
    print(len(pairs))
    best_error = 1e-7
    best_ab = best_cd = None
    i, j = 0, len(pairs)-1
    while i <= j:
        error = pairs[i] + pairs[j] - pi

        if abs(error) < best_error:
            best_error = abs(error)
            best_ab, best_cd = pairs[i], pairs[j]
            print(pairs[i], pairs[j], error)

        if error > 0: j -= 1
        else: i += 1

    s = 0
    # recover a, b, c, d
    for a in range(k_max):
        for b in range(a, k_max):
            fnab = fn[a] + fn[b]
            # handles c, d symmetrically
            if isclose(fnab, best_ab) or isclose(fnab, best_cd):
                print(a, b)
                s += a**2 + b**2

    return s

print(g(10000))
