x = 1
s = "0"
while len(s) <= 1000000:
    s += str(x)
    x += 1

n = 1
for i in range(7):
    n *= int(s[10**i])

print(n)