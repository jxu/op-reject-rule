from math import factorial
from number import prod
from collections import Counter

def partition(n, m=1):  # m = minimum new num size
    if n == 0: return [[]]
    r = []
    for i in range(m, n+1):
        for l in partition(n-i, i):
            r.append([i] + l)

    return r

def S(k):
    s = 0
    for part in partition(k):
        # layouts
        c = factorial(k) // prod(factorial(x) for x in part)

        l = len(part)
        j = prod(range(9,9-l,-1)) # digit assignments without 0
        # handle overcounting identical looking strings
        counter = Counter(part)
        for v in counter.values():
            j //= factorial(v)

        print(part, j, c)

        t = c * (c-1) // 2  # sum of counting strictly larger elems

        r = j * t
        s += r

        # with 0

        for x in counter.keys(): # assign 0 to letter appearing once, twice, etc.
            counter[x] -= 1
            j = prod(range(9, 9-(l-1), -1))  # digit assignments

            for v in counter.values():
                j //= factorial(v)

            c0 = c * (k - x) // k  # prop not starting with 0
            print(j, c0)

            s += j * (c0-1)*c0 // 2


            counter[x] += 1  # restore

    return s


print(S(12))

