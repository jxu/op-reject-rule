# use RPN to avoid parentheses
# any expression tree can map to RPN of
# perm(a, b, c, d) + perm(3 ops)
from itertools import product, permutations

def rpn(expr):
    s = []
    for t in expr:
        if isinstance(t, int):
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


def longest_consecutive(a, b, c, d):
    targets = set()

    for op_set in product(('+', '-', '*', '/'), repeat=3):
        for val_set in permutations((a, b, c, d)):
            expr = val_set + op_set
            try:
                r = rpn(expr)
                # assume float operation returns exact int
                if r > 0 and r == int(r):   
                    targets.add(int(r))
            except: pass

    x = 1
    while x in targets:
        x += 1

    return x-1


max_n = 1
max_digits = None

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                n = longest_consecutive(a, b, c, d)
                print(f"{a}{b}{c}{d} {n}")
                if n > max_n:
                    max_n = n
                    max_digits = f"{a}{b}{c}{d}"

print(max_digits)
