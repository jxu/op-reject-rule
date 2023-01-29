# digits(x xp y) = digits(x) + digits(y) - 1
# Use sieve of Eratosthenes, but stop searching j once xor product is >= 2*n
# since i xp j will have too many digits

def xor_product(x, y):
    r = 0
    while y:
        if y & 1:
            r ^= x
        x <<= 1
        y >>= 1
    return r

n = 1 << 27
s = [0] * n
for i in range(2, n):
    if s[i] == 0:
        for j in range(2,n):
            xp = xor_product(i,j)
            if xp >= 2*n:
                break
            if xp < n:
                s[xp] = 1

print([i for i in range(2, n) if s[i] == 0][5000000-1])
