# For n = q*d + r, by def r < d
# Possible (increasing) geometric sequences: r,d,q  r,q,d  q,r,d
# (The last case is impossible: Let q,r,d = r/a,r,ar.
# Then m^2 = n = (r/a)*(ar) + r = r^2 + r, so m^2 - r^2 = (m-r)(m+r) = r)
# The q and d end up interchangable in q*d.
#
# Let r, d, q = r, a*r, a^2*r.
# The only caveat is a can be rational; Let a = b/c.
# d = a r = b r / c, so c | r
# q = a^2 r = b^2 r / c^2, so c^2 | r
# n = d q + r = b^3 r^2 / c^3 + r < N. Can brute force from here, since
# there's only r = O(sqrt N), and then not many b and c possible.

from number import is_square

def f(N):
    s = set()
    r = 1
    while r + r**2 < N:  # r up to O(N^1/2)
        # optimization: if r is not mult of 4, skip even c
        # skipping mult of 3 is possible but not as nice
        inc = 2 if r % 4 else 1
        for c in range(1, int(r**0.5)+1, inc):
            if r % (c**2): continue
            b = c + 1  # b up to something small
            while True:
                d = b * (r // c)
                q = d * b // c
                n = d * q + r
                if n >= N: break
                
                if is_square(n):
                    print(r, d, q, n)
                    s.add(n)

                b += 1
        r += 1

    return sum(s)

print(f(10**12))
