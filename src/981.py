from number import fact_range, mod_inv_range

M = 888_888_883 
FACT = fact_range(M)
MOD_INV = mod_inv_range(M)

def N(X, Y, Z):
    n = X + Y + Z
    
    if not (X % 2 == Y % 2 == Z % 2):
        return 0

    r = (FACT[n] * MOD_INV[2] *
        MOD_INV[FACT[X]] * MOD_INV[FACT[Y]] * MOD_INV[FACT[Z]]) % M

    # correction factor
    if n % 2 == 0:
        r += ((-1)**(n//2) * FACT[n//2] * MOD_INV[2] * 
              MOD_INV[FACT[X//2]] * MOD_INV[FACT[Y//2]] * MOD_INV[FACT[Z//2]])
            

    return r % M

s = 0
for i in range(88):
    for j in range(88):
        for k in range(88):
            s = (s + N(i**3, j**3, k**3)) % M
print(s)
