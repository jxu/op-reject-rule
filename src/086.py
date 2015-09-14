# Over-complicated (not brute-force) solution: 4 variables (k is a distance along side x)
# Minimize d = sqrt(y^2 + k^2) + sqrt(z^2 + (x-k)^2)
# Some calculus later: k = xy/(y+z),  d^2 = x^2 + (y+z)^2
# Minimized dist when x >= y, z

N_MAX = 6000

squares = set(x**2 for x in range(int(5**0.5 * N_MAX)))  # Max square = 5 * n^2
M = [0] * N_MAX

def M_x(n):
    int_count = 0
    x = n
    for yz in range(2, 2*x+1):  # yz = possible y+z values
        if x**2 + yz**2 in squares:
            if yz <= x + 1:
                int_count += yz // 2
            else:
                int_count += x - (yz+1)//2 + 1

    M[n] = M[n-1] + int_count


for i in range(N_MAX):
    M_x(i)
    if M[i] > 1000000:
        print(i, M[i])
        break
