# a^2 + b^2 = c^2 + d^2, c^2 - b^2 = e^2, a^2 - c^2 = f^2
from number import is_square_fp
MAX_TEST = 1000
min_sum = 10**10

for a in range(1, MAX_TEST):
    a2 = a**2

    for c in range(a%2, a, 2):
        c2 = c**2
        if not is_square_fp(a2 - c2): continue

        for b in range(a%2, c, 2):
            if b == 0: continue
            b2 = b**2
            if not is_square_fp(c2 - b2): continue
            if not is_square_fp(a2 + b2 - c2): continue
            if (a2-b2)//2 >= c2: continue

            a, b, c = (a2+b2)//2, (a2-b2)//2, (c2 - (a2+b2)//2)
            print(a, b, c)
            min_sum = min(min_sum, a+b+c)

print(min_sum)