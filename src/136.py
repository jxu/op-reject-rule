# y(4a-y) = n, y > a
def f(max_n):
    d = [0]*(max_n+1)
    for y in range(1, max_n+1):
        for a in range(1, y):
            x = y*(4*a-y)
            if x > max_n: break
            if x > 0: d[y*(4*a-y)] += 1

    return d

print(f(5000000).count(1))

