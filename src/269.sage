K = 16
R.<x> = PolynomialRing(ZZ)

y = 2
ef = 1
eg = 1
for i in range(0, K):
    if i % 2 == 0:
        ef *= 1 - x^(10 * y^i)
        eg *= 1 - x^(y^i)


print(ef)
print(eg)

print(ef / eg)