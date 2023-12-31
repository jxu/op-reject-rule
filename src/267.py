from math import comb

def chance(f):
    c = 0
    for heads in range(1001):
        if (1+2*f)**heads * (1-f)**(1000-heads) >= 10**9:
            c += comb(1000, heads) / (2 ** 1000)

    return c

# Manually found range of f. Optimal at about 15/100
for f in range(1, 51):
    print(f, "{:.12f}".format(chance(f/100)))