
LINES = ((1,5,9),)

def bad(s, n):
    if not s: return False
    for line in LINES:
        if (line[1] not in s and  # change to line[1,2] not in s for 4-line
            (s[-1] == line[0] and n == line[-1]) or
                (s[-1] == line[-1] and n == line[0])):  # rev seq
            return True
    return False

def f(rem):
    yield []  # end seq here
    if not rem: return

    for n in rem:
        new_rem = rem[:]
        new_rem.remove(n)
        for s in f(new_rem):
            if not bad(s, n):
                yield s + [n]

sols = list(f([1,5,9]))
print(sols)
print(len(sols))