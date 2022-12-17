# RNG ensures no pair of points have same x or y coord
s = [290797]
P = []
for n in range(2000000*2):
    s.append(s[-1]**2 % 50515093)
    if n % 2 == 0:
        P.append(s[-2:])


def dist(p0, p1):
    return ((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)**0.5

# requires sorted points sorted by x
def closest_pair(Px):
    n = len(Px)
    if len(Px) < 2: return float("inf")
    if len(Px) == 2: return dist(Px[0], Px[1])

    m = n//2
    d = min(closest_pair(Px[:m]),
            closest_pair(Px[m:]))
    L = (Px[m-1][0] + Px[m][0])/2  # midway line
    #print(L)
    Pstrip = [p for p in Px if abs(p[0] - L) < d]
    Sy = sorted(Pstrip, key=lambda p:p[1])
    #print(Sy)

    for i in range(len(Sy)):
        for j in range(1, 16):
            if i+j < len(Sy):
                d = min(dist(Sy[i], Sy[i+j]), d)

    return d

Px = sorted(P, key=lambda p:p[0])

#Px = ((-4,1), (-1,1), (1,0), (4,0))
#print(Px)

print(round(closest_pair(Px),9))