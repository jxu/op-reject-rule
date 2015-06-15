import number
pfl = [len(set(number.prime_factors(n))) for n in range(500000)]
for i in range(1, 500000-4):
    if 4 == pfl[i] == pfl[i+1] == pfl[i+2] == pfl[i+3]:
        print(i)
        break
