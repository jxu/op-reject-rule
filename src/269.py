from collections import defaultdict

def brute(x):
    for a in range(100000):
        y = 0
        t = a
        for d in str(a):
            y = x * y + int(d)


        if y == 0:
            yield a

sols = defaultdict(list)

for x in range(-9, 0):
    for a in brute(x):
        print(x, a)
        sols[a].append(x)

for a in sols:
    if len(sols[a]) > 1:
        print(a, sols[a])