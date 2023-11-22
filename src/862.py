from number import prod

# important to not get bogged down in math.factorial calls
FACT = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
        479001600)

def make_hists(N, min_d=0, depth=0):
    if depth == N:
        return [[0] * 10]

    new_hists = []
    for d in range(min_d, 10):
        for hist in make_hists(N, d, depth + 1):
            new_hist = hist[:]
            new_hist[d] += 1
            new_hists.append(new_hist)

    return new_hists


def S(N):
    s = 0
    for hist in make_hists(N):
        c = (FACT[N] // prod(FACT[hist[i]] for i in range(10)) *
             (N - hist[0]) // N)
        s += c * (c-1) // 2

    return s

print(S(12))