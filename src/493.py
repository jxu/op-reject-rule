# Approx 6.818
import math, number


def create_combo(combo, combos, last):
    if sum(combo) == 20:
        combos.append(combo)

    if sum(combo) < 20 and len(combo)+1 <= 7:
        for i in range(last, 11):
                create_combo(combo + [i], combos, i)


combos = []
create_combo([], combos, 1)
s = 0
o = 0
for c in combos:
    colorings = number.combination(7, len(c))

    orderings = colorings

    for g in c:
        orderings *= number.combination(10, g)

    print(c, orderings)
    o += orderings
    s += len(c)*orderings


print(s, o, str(s/o))