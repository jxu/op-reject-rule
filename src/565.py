# Divisor sum function = sigma(n), is multiplicative
# Implement sigma efficiently later in number.py?
# sigma(i) = 2017*k = sigma(a)*sigma(b), sigma(a) = 2017 and a, b coprime

# Simple method
def sigma(n):
    s = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n//i == i: s += i
            else: s += i + n//i

    return s

def S(n, d):
    for j in range(2, n+1):
        if sigma(j) == d:
            print(j)

print(S(20, 7))