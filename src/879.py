
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
for line in COMPACT_LINES:
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

def f(rem):
    yield []  # end seq here
    if not rem: return

    for n in range(16):
        if not (rem & (1 << n)): continue

        for s in f(rem ^ (1 << n)):
            if not bad(s, n):
                s.append(n)
                yield s


sols = filter(lambda x: len(x) >= 2, f(0xffff))
r = 0
for sol in sols:
    if r % 100000 == 0: print(''.join(hex(n)[2] for n in sol).rjust(16))
    r += 1
print(r)