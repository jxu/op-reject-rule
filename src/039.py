max_s = max_p = 0
for p in range(1001):
    s = 0
    for a in range(2, p//4):
        for b in range(a+1, p//2):
            if a**2 + b**2 == (p-a-b)**2:
                s += 1

    print(p, s)
    if s > max_s:
        max_s = s
        max_p = p

print(max_p)
