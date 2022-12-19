# Brute-force: check some near points by x-coordinate
# For random-ish distribution of points, closest pair will have close x coord
B = 10

def dist(p0, p1):
    return abs(p0 - p1)

def d(k):
    s = [290797]
    P = []
    for n in range(2*k):
        s.append(s[-1]**2 % 50515093)
        if n % 2 == 0:
            P.append(s[-2] + s[-1]*1j)

    D = float("inf")
    Px = sorted(P, key=lambda p:p.real)

    for i in range(k):
        for j in range(max(0, i-B), min(k, i+B)):
            if i == j: continue
            D = min(D, dist(Px[i], Px[j]))

    return D

print(round(d(2000000),9))