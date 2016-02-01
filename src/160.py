def f(N):
    r = 1
    for i in range(1, N+1):
        r *= i
        while not r % 10:
            r //= 10
        r = r % 10**10

    return r

def f(a, b):
    s = 1
    for i in range(a, b+1):
        s *= i
        while not s % 10:
            s //= 10
        s = s % 10**10
    return s

print(f(1, 1000))