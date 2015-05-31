s = 0

for i in range(1000, 10000): # Must be 4 digits
    if all(str(i).count(d) == 1 for d in str(i)): # Unique digits
        for j in range(2, 1000):
            if i % j == 0:
                combo = str(i) + str(j) + str(i//j)
                if len(combo) == 9 and set(combo) == set("123456789"):
                    print(i, j, i//j)
                    s += i
                    break

print(s)
