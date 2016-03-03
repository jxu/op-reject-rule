# y(4a-y) = n, y > a
def f(max_n):
    d = [0]*(max_n+1)
    for y in range(1, max_n+1):
        if y%100000 == 0: print(y)
        for a in range(y//4, y):  # Skip entire neg range
            x = y*(4*a-y)
            if x > max_n: break
            if x > 0:
                d[x] += 1

    return d

print(f(50000000).count(1))
