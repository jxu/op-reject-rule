def P(n):
    l = range(1, n+1)
    if len(l) == 1: return l[0]
    while True:
        l = l[1::2]
        if len(l) == 1: return l[0]
        l = l[len(l)%2::2]
        if len(l) == 1: return l[0]


for i in range(1, 51):
    print(P(i), i, ((i+1)/2 - P(i))*2)