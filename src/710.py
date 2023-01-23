from number import memoize

M = 1000000

@memoize
def f(rem, two_seen):
    s = 0
    if rem == 0:
        if two_seen: return 1
        else:
            return 0

    # end building immediately by placing middle digit
    two_seen_new = rem == 2
    if two_seen or two_seen_new:
        s += 1

    for i in range(1, rem//2+1):
        if i == 2: two_seen_new = True
        else: two_seen_new = two_seen

        s = (s + f( rem-2*i, two_seen_new)) % M

    return s


def t(n):
    s = f( n, False) % M
    return s


for n in range(43, 100000):
    tn = t(n)
    print(n, tn)
    if tn == 0:
        print(n)
        break

