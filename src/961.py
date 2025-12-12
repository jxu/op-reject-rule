from functools import cache

def remove_bit(x, d):
    lomask = (1 << d) - 1
    himask = (~lomask) << 1

    return (x & lomask) | ((x & himask) >> 1)

n = 18

# negamax
@cache
def f(x):
    if x == 0: return -1
    for d in range(x.bit_length() ):
        if - f(remove_bit(x, d)) == 1:
            return 1
    return -1

s = 0
for x in range(2**n):
    if f(x) == 1:
        s += 9 ** (x.bit_count())

print(s)
