from number import memoize

M = 1000000

@memoize
def s(n):
    if n < 2: return 0
    return s(n-2) + t(n)

@memoize
def t(n):
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 0

    return t(n-2) + 2**((n-4)//2) + sum(t(n-2*i) for i in range(3, n//2+1))


for n in range(1, 21):
    tn = t(n)

    print(n, tn)


