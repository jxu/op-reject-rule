# Related to A249347
# Empirical testing
def factors_7(n):
    x = 1
    f = 0
    while 7**x <= n:
        f += n // 7**x
        x += 1
    return f

z = 0
last_s = 0
for r in range(0, 200):
    s = 0
    j = ['.'] * (r+1)
    for n in range(r+1):
        if factors_7(r) - (factors_7(n) + factors_7(r-n)) >= 1:
            j[n] = 'X'
            s += 1
    #print(r, s, s-last_s)
    print(r+1, ' '*(5-len(str(r+1))), "".join(j))
    last_s = s
    z += s

s=0
for i in range(10**7):
    s += i
print(s)