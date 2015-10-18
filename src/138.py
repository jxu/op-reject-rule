squares = set(i**2 for i in range(1000))
for b in range(2, 1000000, 2):
    L1 = (b//2)**2 + (b+1)**2
    L2 = (b//2)**2 + (b-1)**2

    if L1 in squares:
        print("L", L1**0.5)
    if L2 in squares:
        print(L2**0.5)