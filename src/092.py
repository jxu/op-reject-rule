# More chainz
# Max 9*9*6 = 567
chains = [0] * 600

def square_sum(n):
    return sum(int(c)**2 for c in str(n))

for i in range(1, 600):
    n = i
    while n not in (1, 89):
        if chains[n] in (1, 89):
            n = chains[n]
            break

        n = square_sum(n)

    chains[i] = n

print(sum(chains[square_sum(i)] == 89 for i in range(1, 10**7)))
