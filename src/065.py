# A-1 = 1, B-1 = 0;  A0 = b0, B0 = 1
A = [1, 2]
B = [0, 1]
for i in range(100):
    b = (1, 2*(i+2)//3, 1)[i%3]
    A.append(b*A[-1] + A[-2])
    B.append(b*B[-1] + B[-2])

print(sum(map(int, str(A[100]))))
