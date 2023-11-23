from math import prod

# important to not repeatedly do math.factorial calls
FACT = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800,
        479001600)


# trying out generator to save memory
# also aryanc403 idea: use DP to return sum of c, c^2?
def make_hists(N, min_d=0):
    if N == 0:
        yield [0] * 10
        return

    for d in range(min_d, 10):
        for hist in make_hists(N-1, d):
            hist[d] += 1
            yield hist


def T(N, hist):
    c = (FACT[N] // prod(FACT[hist[i]] for i in range(10)) *
         (N - hist[0]) // N)
    return c * (c-1) // 2


def S(N):
    return sum(T(N, hist) for hist in make_hists(N))

print(S(12))
