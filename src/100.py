# For n/m, (n/m)((n-1)/(m-1)) = 1/2
# 2n^2 + 2n = m^2 + m,  =>  n = (sqrt(2m^2 + 2m + 1) - 1)/2

def is_square(n):
    print(round(n**0.5)**2, n)
    return round(n**0.5)**2 == n
    see SE

m = 10**12
while True:
    break
    x = ((2*m**2 + 2*m + 1)**0.5 - 1)/2
    use integer methods for is_square
    if round((2*m**2 + 2*m + 1)**0.5)**2 == (2*m**2 + 2*m + 1) and x.is_integer():
        print(x, m)
        break
    m += 1

print(is_square(12345678987654321234567 ** 2))