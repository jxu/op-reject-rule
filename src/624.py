from number import cache, mod_inv

# Probably can go in number functions
@cache
def fibmod(n, m):
    if n <= 1: return n 
    if n == 2: return 1

    fh = fibmod(n//2, m)
    fh1 = fibmod(n//2 + 1, m)
    
    if n % 2 == 0:
        return (fh * (2 * fh1 - fh)) % m
    else:
        return (fh1**2 + fh**2) % m


def lucasmod(n, m):
    if n == 0: return 2
    return (fibmod(n+1, m) + fibmod(n-1, m)) % m


def Q(n, p):
    a = pow(2, n, p) * fibmod(n-1, p) + (-1)**(n-1)
    b = pow(4, n, p) - pow(2, n, p)*lucasmod(n, p) + (-1)**n

    return (a % p) * mod_inv(b, p) % p

print(Q(10**18, 10**9 + 9))
