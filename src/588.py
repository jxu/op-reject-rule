# A247649. Solution using a genralization of the Run Length Transform,
# N. J. A. Sloane, On the Number of ON Cells in Cellular Automata, arXiv:1503.01168
from number import product

def create_tri(n):
    # Calculate using generalized Pascal's identity
    # Creates right half of centered triangle
    # T(k+1,c) = T(k,c-2) + T(k,c-1) + T(k,c) + T(k,c+1) + T(k,c+2)
    row = [1] + [0]*(2*n+2)
    for k in range(1, n+1):
        l = row[:]
        for c in range(2*k + 1):
            row[c] = (l[abs(c-2)] + l[abs(c-1)] + l[c] + l[c+1] + l[c+2]) % 2

    return 2*row.count(1) - 1


def a(n):
    print(n)
    s = [int(d, 2) for d in bin(n)[2:].split("00") if d != '' and d != '0']
    print(s)

    return product(create_tri(m) for m in s)

print(sum((a(10**k) for k in range(1, 19))))
