import numpy as np

N = 10

a = [0]
b =[0]
s = 102022661
for n in range(1, 21):
    print(s)
    if n % 2:
        a.append(s)
    else:
        b.append(s)

    s = (s*s) % 998388889

print(a)
print(b)

A = np.ones((N+1,N+1), dtype=np.int64) * 10**12
D = np.full((N+1,N+1), ' ', dtype=bytes)

for i in range(1, N+1):
    for j in range(1, N+1):
        if (i,j) == (1,1):
            A[i][j] = a[i]+b[j]
        else:
            A[i][j] = a[i] + b[j] + min(A[i-1][j], A[i][j-1])
            if A[i-1][j] < A[i][j-1]:
                D[i][j] = 'V'
            else:
                D[i][j] = '>'

print(A)
print(D)

