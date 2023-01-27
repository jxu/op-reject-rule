from number import memoize

M = 1000000

@memoize
def F(rem, two_seen):
    if rem < 0: return 0
    if rem == 0:
        return 1 if two_seen else 0
    return f(rem, two_seen) + F(rem-2, two_seen)



@memoize
def f(rem, two_seen):
    s = 0
    if rem < 0: return 0
    if rem == 0:
        return 1 if two_seen else 0

    # end building immediately by placing middle digit
    if two_seen or rem == 2:
        s += 1

    s = (s + f(rem - 2, two_seen) + f(rem - 4, True) + F(rem-6, two_seen)) % M

    return s


def t(n):
    s = f(n, False) % M
    return s


for n in range(43, 10000000):
    tn = t(n)
    if tn == 0:
        print(n)
        break
    print(n, tn)


