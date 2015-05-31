n = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0): n += i
print(n)

# One-liner
print(sum(i for i in range(1000) if 0 in (i%3, i%5)))