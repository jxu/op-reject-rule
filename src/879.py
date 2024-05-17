from functools import cache

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

def bad(s, n):
    if not s: return False
    for line in LINES:
        # check endpoints of line
        if (s[-1] == line[0] and n == line[-1]) or \
            (s[-1] == line[-1] and n == line[0]):

            if len(line) == 4:
                if line[1] not in s or line[2] not in s:
                    return True
            else:
                if line[1] not in s:
                    return True
    return False

@cache
def f(used, last):
    print("{:09b}".format(used), last)


    r = 0

    assert used & (1 << last)
    if used == 1 << last: return 1

    for d in range(9):
        if d == last: continue
        mask = 1 << d
        if not (used & mask): continue

        bad = False
        for line in LINES:
            if ({last,d} == {line[0], line[2]} and not (used & (1 << line[1])) ):
                bad = True

        if not bad:
            r += f(used & ~(1 << last), d)


    return r


print(sum(f(0x1ff, d) for d in range(9)))
