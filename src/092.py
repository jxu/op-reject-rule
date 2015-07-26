# More chainz
s = 0
chains = [0] * 10**7
for i in range(1, 10**7):
    n = i
    while n not in (1, 89):
        if chains[n] in (1, 89):
            n = chains[n]
            break

        n = sum(int(c)**2 for c in str(n))

    chains[i] = n
    if n == 89: s += 1

print(s)
