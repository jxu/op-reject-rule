# PQa Algorithm http://www.jpr2718.org/pell.pdf
def min_pell(D, max_recurse=1000):
    m = max_recurse
    P=[0]*m; Q=[0]*m; A=[0]*m; B=[0]*m; G=[0]*m; a=[0]*m
    P[0] = 0; Q[0] = 1
    A[-2] = 0; A[-1] = 1
    B[-2] = 1; B[-1] = 0
    G[-2] = -P[0]; G[-1] = Q[0]

    for i in range(m - 2):
        if i >= 1:
            P[i] = a[i-1]*Q[i-1] - P[i-1]
            Q[i] = (D - P[i]**2) // Q[i-1]

        a[i] = int((P[i] + D**0.5)/Q[i])
        A[i] = a[i]*A[i-1] + A[i-2]
        B[i] = a[i]*B[i-1] + B[i-2]
        G[i] = a[i]*G[i-1] + G[i-2]

        if A[i]**2 - D*B[i]**2 == 1:
            return A[i]

    print("Max recurse reached")


max_x = 0
max_D = 0
squares = [n**2 for n in range(32)]
for D in range(1001):
    if D not in squares:
        if min_pell(D) > max_x:
            max_x = min_pell(D)
            max_D = D

print(max_D)