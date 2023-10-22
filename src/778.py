c = [0] * 10

for i in range(8):
    for j in range(8):
        c[(i*j)%10] += 1

print(c)

print(sum(i*c[i] for i in range(10)))
