# From the example, for spots in a line like 1-5-9, 1-9 or 9-1 can only occur
# if 5 appeared before in the sequence.
# From there, it is DP keeping track of the new spot and
# previously used spots (not including new spot).
# Used spots are a bitset which allows hashing in python.
# The length 3 and 4 lines are hardcoded because it's not that much nicer to
# code all the line indexing. (plus some fun with hex)

from functools import cache

MODE_3x3 = False

if MODE_3x3:
    N = 9
    # 0 1 2
    # 3 4 5
    # 6 7 8
    COMPACT_LINES = ("012", "345", "678", "036", "147", "258", "048", "246")

else:
    N = 16
    # 0 1 2 3
    # 4 5 6 7
    # 8 9 A B
    # C D E F
    COMPACT_LINES = \
        ("048", "48C", "048C",  # vertical
         "159", "59D", "159D",
         "26A", "6AE", "26AE",
         "37B", "7BF", "37BF",
         "012", "123", "0123",  # horizontal
         "456", "567", "4567",
         "89A", "9AB", "89AB",
         "CDE", "DEF", "CDEF",
         "258", "369", "69C", "369C", "7AD",  # diagonal
         "16B", "05A", "5AF", "05AF", "49E"
         )


LINES = [[int(c,16) for c in line] for line in COMPACT_LINES]
print(list(LINES))

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

