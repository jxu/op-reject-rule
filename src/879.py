
LINES = ((1,5,9),(2,5,8),(3,5,7),(4,5,6),
         (1,4,7),(3,6,9),(1,2,3),(7,8,9))

def bad(s, n):
    if not s: return False
    for line in LINES:
        if (line[1] not in s and  # change to line[1,2] not in s for 4-line
                ((s[-1] == line[0] and n == line[-1]) or
                (s[-1] == line[-1] and n == line[0]))):  # rev seq
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

nums = list(range(1,10))
sols = list(filter(lambda x: len(x) >= 2, f(nums)))
for sol in sols:
    print(''.join(map(str,sol)))
print(len(sols))