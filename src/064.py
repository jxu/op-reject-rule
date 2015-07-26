# (066 copy) PQa Algorithm http://www.jpr2718.org/pell.pdf
def min_pell_period(D, max_recurse=1000):
    m = max_recurse
    seen = []
    P, Q, A, B, G, a = [0]*m, [0]*m, [0]*m, [0]*m, [0]*m, [0]*m
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
            pass

        if (P[i], Q[i], a[i]) in seen:
            return len(seen) - 1
        else:
            seen.append((P[i], Q[i], a[i]))

    print("Max recurse reached")


squares = [x**2 for x in range(101)]
odd = 0
for N in range(2, 10001):
    if N not in squares:
        if min_pell_period(N) % 2 == 1:
            odd += 1

print(odd)
