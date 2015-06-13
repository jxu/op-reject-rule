m = 0
for i in range(1, 10**5):
    s = ""
    for j in range(1, 10):
        s += str(i*j)
        if len(s) >= 9: break

    if len(s) == 9 and set(s) == set("123456789"):
        m = max(m, int(s))

print(m)
