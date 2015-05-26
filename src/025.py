a = b = i = 1
while a < 10**999:
    a, b = b, a+b
    i += 1
print(i)
