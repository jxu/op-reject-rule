

p3 = [n*(n+1)//2 for n in range(200)]
p4 = [n**2 for n in range(200)]
p5 = [n*(3*n-1)//2 for n in range(200)]
p6 = [n*(2*n-1) for n in range(200)]
p7 = [n*(5*n-3)//2 for n in range(200)]
p8 = [n*(3*n-2) for n in range(200)]

def foo(current, seen):
    if len(seen) == 6:
        print(current)
        break
    
