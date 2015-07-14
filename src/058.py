from number import is_prime

s, n = 2, 1
a = 0
for i in range(10**5):
    if is_prime(n): a += 1
    if i%1000 == 0: print(s, a/(i+1))
    if i%4 == 0 and a/(i+1) < 0.10 and s > 7:
        print(s+1)
        break

    if i%4 == 0 and i != 0: s += 2
    n += s