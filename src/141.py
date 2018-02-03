# q*d + r = n;  must be r,d,q or r,q,d
# (d^3)/r + r = a^2

LIMIT = 10**5
squares = set(i*i for i in range(1, int(LIMIT**0.5)+1))
s = set()

for d in range(1, int(LIMIT**0.5)):
    d3 = d**3
    for r in range(d-1, 0, -1):
        if d3/r + r > LIMIT: break
        if d3 % r == 0:
            if d3 // r + r in squares:
                print(d, r, d/r)
                s.add(d3 // r + r)

print(sum(s))