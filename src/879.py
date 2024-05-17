from functools import cache

N = 16

COMPACT_LINES3 = ("012", "345", "678", "036", "147", "258", "048", "246")

COMPACT_LINES = \
    ("048", "48C", "048C",
     "159", "59D", "159D",
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

# a little abstraction
def in_bit(b, i):
    return bool(b & (1 << i))

def clear_bit(b, i):
    return b & ~(1 << i)

def valid(used, last, d):
    for line in LINES:
        if ((last == line[0] and d == line[-1]) or
                (last == line[-1] and d == line[0])):  # line endpoints

            if not in_bit(used, line[1]):
                return False

            if len(line) == 4 and not in_bit(used, line[2]):
                return False
    return True

@cache
def f(used, new_digit):
    if not used: return 1
    r = 0
    for d in range(N):
        if not in_bit(used, d): continue

        if valid(used, new_digit, d):
            r += f(clear_bit(used, d), d)

    return r


s = -N  # exclude length 1 passwords
for used in range(1 << N):  # 0000 to FFFF
    for d in range(N):
        if not in_bit(used, d):
            s += f(used, d)

print(s)

