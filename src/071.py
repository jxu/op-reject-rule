min_dif = 1
for d in range(10**6 - 10, 10**6):
    if d%7 != 0:
        n = int(3*d/7)
        if 3/7 - n/d < min_dif:
            num = n
            min_dif = 3/7 - n/d

print(num)