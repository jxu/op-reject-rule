# Kempner function. A002034
# s(p1^a1 * ... * pk^ak) = max(s(p1^a1), ..., s(pk^ak))
# So calculate all s(p^a)
# Then for every multiple of p, calculate  max p^a that divides it (ruler)
# and store max s(p^a) along the way

# Profiler told me memoizing actually slows down function!
# Timings with pypy: 81.1s
# Removing @memoize: 58.4s
# Pre-calculating ruler_full: 23.4s

from number import sieve, ruler

def s(p, a):  # s(p^a)
    if a <= p: return a*p
    # Count multiples of p until the factorial has enough multiples of p
    l = 0
    m = 0
    while m < a:
        l += p
        m += ruler(l, p)

    return l


def S(n):
    primes = sieve(n)
    sl = [0]*(n+1)

    ruler_full = [0]*(n+1)

    for p in primes:
        # Find ruler(k, p) for all values and store in array for fast access
        for i in range(p, n+1, p):
            ruler_full[i] = 0
        pp = p
        while pp <= n:
            for i in range(pp, n + 1, pp):
                ruler_full[i] += 1
            pp *= p

        for k in range(p, n+1, p):
            sl[k] = max(sl[k], s(p, ruler_full[k]))

    return sum(sl)


print(S(10**8))