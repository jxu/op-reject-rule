# Uninteresting brute force on possible ascending digit nums
# See solution thread for constant-time solution!

M = 1123455689

def g(max_d, digits_left):
    if not digits_left:
        yield 0; return

    for d in range(max_d+1):
        for s in g(d, digits_left-1):
            # build right-to-left. faster than string ops
            yield 10*s + d


def S(n):
    fact = [1] * (n + 1)
    for i in range(2, n+1):
        # runs just as fast without using mod arithmetic
        fact[i] = (i * fact[i-1])

    r = 0
    for m in g(9, n):
        s = str(m).zfill(n)
        x = fact[n]
        for d in range(10):
            x //= fact[s.count(str(d))]
        r += m*x

    return r

print(S(18) % M)