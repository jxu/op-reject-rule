# Period appears to be 2a
def r_max(a):
    mr = 0
    for n in range(2*a):
        r = pow(a-1, n, a**2) + pow(a+1, n, a**2)
        mr = max(mr, r % a**2)
    return mr

print(sum(r_max(a) for a in range(3, 1001)))