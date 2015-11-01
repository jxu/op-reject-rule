def f(N):
    r = 1
    for i in range(1, N+1):
        r *= i
        while not r % 10:
            r //= 10
        r = r % 10**10

    return r

print(f(10**6))
#print(pow(f(10**6), 10))

print(f(10**5))