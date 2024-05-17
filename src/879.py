from functools import cache

N = 9

COMPACT_LINES3 = (
    "012", "345", "678", "036", "147", "258", "048", "246"
)

COMPACT_LINES = \
    ("048", "48C", "048C",
     "159", "590", "1590",
     "26A", "6AE", "26AE",
     "37B", "7BF", "37BF",
     "012", "123", "0123",
     "456", "567", "4567",
     "89A", "9AB", "89AB",
     "CDE", "DEF", "CDEF",
     "258", "369", "69C", "369C", "7AD",
     "16B", "05A", "5AF", "05AF", "49E"
     )

LINES = []
for line in COMPACT_LINES3:
    LINES.append([int(c,16) for c in line])

print(LINES)

def valid(last, d):
    for line in LINES:
        if ({last, d} == {line[0], line[2]} and not (used & (1 << line[1]))):
            return False
    return True

@cache
def f(used_before_last, last):
    print("{:09b}".format(used_before_last), last)
    if not used_before_last: return 1
    r = 0
    for d in range(N):
        mask = 1 << d
        if not (used_before_last & mask): continue

        if valid(last, d):
            r += f(used_before_last & ~(1 << d), d)

    return r


s = -N  # exclude length 1 passwords
for used in range(1 << N):
    for d in range(N):
        if not (used & (1 << d)):
            s += f(used, d)

print(s)

