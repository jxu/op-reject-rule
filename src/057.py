# Fundamental recurrence formula, x = A/B
s = 0
A = [1, 3]
B = [1, 2]

for i in range(1000-1):
    A.append(2*A[-1] + A[-2])
    B.append(2*B[-1] + B[-2])
    if len(str(A[-1])) > len(str(B[-1])): s += 1

print(s)
