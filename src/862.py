from number import prod

# important to not repeatedly do math.factorial calls
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


def T(N, hist):
    c = (FACT[N] // prod(FACT[hist[i]] for i in range(10)) *
         (N - hist[0]) // N)
    return c * (c-1) // 2


def S(N):
    return sum(T(N, hist) for hist in make_hists(N))

print(S(12))
