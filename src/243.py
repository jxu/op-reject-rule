# Very composite numbers
# Solution generating from prime bases
from number import phi
prime_base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
min_d = 10**20

def gen_exp(l, limit):
    if len(l) == len(prime_base):
        d = 1
        for i in range(len(prime_base)):
            d *= prime_base[i] ** l[i]
        if 1 < d < 963761198400:
            r = phi(d) / (d-1)
            global min_d
            if r < 15499 / 94744 and d < min_d:
                print(d, r)
                min_d = d

    else:
        if len(l) > 4:
            limit = min(limit, 1)
        for i in range(limit+1):
            gen_exp(l + [i], i)

gen_exp([], 8)


# Easy solution (very composite number is much larger than 2*3*5*7*11*13)
for d in range(2*3*5*7*11*13, 10**12, 2*3*5*7*11*13):
    if (phi(d) / (d-1)) < (15499 / 94744):
        print(d)
        break