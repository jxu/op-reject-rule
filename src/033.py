ns = ds = 1
for d in range(10, 100):
    for n in range(10, d):
        if d%10 != 0 and n%10 != 0 and d%11 != 0 and n%11 != 0:
            for c in str(d):
                if str(c) in str(n):
                    dx = int(str(d).replace(str(c), ''))
                    nx = int(str(n).replace(str(c), ''))
                    if n/d == nx/dx:
                        print(nx, dx)
                        ns *= nx
                        ds *= dx

print(ds // ns) # 1/d


