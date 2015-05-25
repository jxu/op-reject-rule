for a in range(500):
    for b in range(a, 500):
        if a**2 + b**2 == (1000-a-b)**2:
            print(a*b*(1000-a-b))