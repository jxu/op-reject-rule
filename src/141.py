# For n = q*d + r, by def r < d
# Possible (increasing) geometric sequences: r,d,q  r,q,d  q,r,d
# (d^3)/r + r = a^2

def is_square(n):
    return round(n**0.5)**2 == n

def f(N):
    s = set()
    r = 1
    while r + r**2 < N:  # r up to O(n^1/2)
        c = 1
        while c**2 <= r:  # c up to O(r^1/2) = O(n^1/4)
            if r % (c**2) == 0:
                b = c + 1
                # b up to something small
                while (n := b**3 * r**2 // c**3 + r) < N:
                    if is_square(n):
                        d = b * r // c
                        q = b * b * r // (c * c)
                        print(r, d, q, n)
                        s.add(n)

                    b += 1
            c += 1
        r += 1

    return sum(s)

print(f(10**12))
