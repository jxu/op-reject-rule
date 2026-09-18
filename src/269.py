def brute(x):
    s = 0
    for a0 in range(10):
        for a1 in range(10):
            for a2 in range(10):
                for a3 in range(10):
                    for a4 in range(10):
                        if a0 + x * (a1 + x * (a2 + x * (a3 + x * a4))) == 0:
                            print(a4, a3, a2, a1, a0)
                            s += 1

    return(s)

#print(brute(-1))

from functools import cache

@cache
def f(x, y, l):

    if l == 0:
        return int(y == 0)

    s = 0
    for a in range(10):
        if (y - a) % x == 0:
            yy = (y - a) // x
            s += f(x, yy, l-1)

    return s

for x in range(-9, 0):
    print(x, f(x, 0, 5))