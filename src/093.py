# Kinda brute force, but with RPN at least no need for parentheses
from itertools import product, permutations

def RPN(eq):
    s = []
    for t in eq:
        if type(t) == int:
            s.append(t)
        else:
            y = s.pop()
            x = s.pop()
            if t == '+': s.append(x+y)
            elif t == '-': s.append(x-y)
            elif t == '*': s.append(x*y)
            elif t == '/':
                assert(y != 0)
                s.append(x/y)

    assert(len(s) == 1)
    return s[0]


def calc(a, b, c, d):
    op_sets = product(('+', '-', '*', '/'), repeat=3)
    targets = set()
    for op_set in op_sets:
        t = [a, b, c, d] + list(op_set)
        for eq in permutations(t):
            # RPN equation must start with 2 numbers and end with operation
            if type(eq[0]) != int or type(eq[1]) != int \
                or type(eq[-1]) != str: continue

            try:
                r = RPN(eq)
                if r > 0 and r == round(r):
                    targets.add(round(r))
            except: pass

    test = 1
    while test in targets:
        test += 1

    return test-1


max_n = 1
max_digits = None

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                n = calc(a, b, c, d)
                print(a, b, c, d, n)
                if n > max_n:
                    max_n = n
                    max_digits = 1000*a + 100*b + 10*c + d

print(max_digits)
