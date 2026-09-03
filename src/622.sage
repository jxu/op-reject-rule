# 2^60 = 1 (mod 2n+1), so consider factors of 2^60 - 1
n = 60
print(sum(d + 1 for d in divisors(2^n - 1) if Mod(2, d).multiplicative_order() == n))
