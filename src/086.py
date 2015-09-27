# Over-complicated (not brute-force) solution: 4 variables (k is a distance along side x)
# Minimize d = sqrt(y^2 + k^2) + sqrt(z^2 + (x-k)^2)
# Some calculus later: k = xy/(y+z)
# => d^2 = x^2 + (y+z)^2  [As euler pointed out, only drawing a net is needed]
# Minimized dist when x >= y, z  [Found empirically]

N_MAX = 2000
squares = set(x**2 for x in range(int(5**0.5 * N_MAX)))  # Max square = 5 * n^2
M = [0] * N_MAX

for x in range(1, N_MAX):  # Build solutions from previous
    int_count = 0
    for yz in range(2, 2*x+1):  # yz = possible y+z values
        if x**2 + yz**2 in squares:
                int_count += min(yz//2, x - (yz-1)//2)  # Count yz values so x >= y, z

    M[x] = M[x-1] + int_count
    if M[x] > 1000000:
        print(x, M[x])
        break
