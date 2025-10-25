# At fraction a/b, min {nx} has slope b until next Farey seq fraction e/f
# EV given by area of triangles with base x = e/f - a/b and height b*x
# Use a method to directly iterate through Farey sequence without recursion
# one simplification is that b*e - a*f = 1, so x*x*b/2 = 1 / (2bf^2)
def F(N):
    s = 0
    # run through Farey sequence, starting with a/b = 0/1 and e/f = 1/N
    a, b, e, f = 0, 1, 1, N

    while (a, b) != (1, 1):
        # next term after a/b and e/f is c/d
        k = (N + b) // f
        c = k * e - a
        d = k * f - b
        s += 1 / (2 * b * f * f)
        
        a, b, e, f = e, f, c, d  # replace with next fracs
    
    return s

print(round(F(10000), 13))

