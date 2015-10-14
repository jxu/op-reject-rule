# Euler's theorem: For coprime a, n, a^phi(n) = 1 mod (n)
# a^phi(10**8) = a^(4*10**7) = 1 mod 10**8
n = 1
for i in range(1855): n = pow(1777, n % (4*10**7), 10**8)
print(n)