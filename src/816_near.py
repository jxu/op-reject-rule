# Lazy method: check some near points by x-coordinate
# For random-ish distribution of points, closest pair will have close x coord
B = 10

def d(k):
    s = 290797
    P = [0]*k
    for n in range(2*k):
        P[n//2] += s * (1j if n%2 else 1)
        s = pow(s, 2, 50515093)

    D = float("inf")
    Px = sorted(P, key=lambda p:p.real)

    for i in range(k):
        for j in range(max(0, i-B), min(k, i+B)):
            if i == j: continue
            D = min(D, abs(Px[i] - Px[j]))

    return D

print(round(d(2000000),9))