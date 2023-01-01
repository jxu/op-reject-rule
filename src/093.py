# consider all possible binary expression trees
# subtraction is non-commutative, non-associative
# (a-b)-(c-d), ((a-b)-c)-d, (a-(b-c))-d, a-((b-c)-d), a-(b-(c-d))
# assume floating point operations are exact (ex. 3 * (1/3) == 1)

from itertools import permutations

def f(x, op, y):
    if   op == '+': return x + y
    elif op == '-': return x - y
    elif op == '*': return x * y
    elif op == '/': return x / y if y else float("nan")  # avoid div by 0


def longest_consecutive(a, b, c, d):
    ops = ('+', '-', '*', '/')
    targets = set()
    for a, b, c, d in permutations((a, b, c, d)):
        for op0 in ops:
            for op1 in ops:
                for op2 in ops:
                    targets.add(f(f(a, op0, b), op1, f(c, op2, d)))
                    targets.add(f(f(f(a, op0, b), op1, c), op2, d))
                    targets.add(f(f(a, op0, f(b, op1, c)), op2, d))
                    targets.add(f(a, op0, f(f(b, op1, c), op2, d)))
                    targets.add(f(a, op0, f(b, op1, f(c, op2, d))))

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
