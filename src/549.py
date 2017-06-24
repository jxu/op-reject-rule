# Kempner function. A002034
# s(p1^a1 * ... * pk^ak) = max(s(p1^a1), ..., s(pk^ak))
# So calculate all s(p^a)
# Then for every multiple of p, calculate  max p^a that divides it (ruler)
# and store max s(p^a) along the way

from number import sieve, memoize, ruler

@memoize
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

    for p in primes:
        for k in range(p, n+1, p):
            sl[k] = max(sl[k], s(p, ruler(k, p)))

    return sum(sl)


print(S(10**8))