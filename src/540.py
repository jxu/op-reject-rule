# Tree of Pythagorean triples (not for solving problem but for future reference)

def generate(a, b, c, max_c):
    if c > max_c: return 0
    #print(a, b, c)
    s = 1
    s += generate( a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c, max_c)
    s += generate( a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c, max_c)
    s += generate(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c, max_c)

    return s

print(generate(3, 4, 5, 1000))
