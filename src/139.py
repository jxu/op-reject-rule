from fractions import gcd
pt = 0
for m in range(1, 7072):  # 2m^2 < 10^8
    for n in range(m%2+1, m, 2):
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        if a+b+c < 10**8 and c % (b-a) == 0 and gcd(m, n) == 1:
            print(a, b, c, 10**8 // (a+b+c))
            pt += 10**8 // (a+b+c)

print(pt)