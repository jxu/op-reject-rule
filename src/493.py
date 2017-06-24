# Approx 6.818 from random testing
# Much simpler solution from Tepsi: Let p = probability of color being in draw
# p = 1 - (60 choose 20)/(70 choose 20). Then total expected is 7p

from number import combination, product
from math import factorial

combos = []

def create_combo(combo, last):
    if sum(combo) == 20:
        combos.append(combo)

    if sum(combo) < 20 and len(combo) < 7:
        for i in range(last, 11):
                create_combo(combo + [i], i)


create_combo([], 1)
s = 0

for combo in combos:
    combo_colors = len(combo)

    # 1. Pick which colors to use in the combo
    colors_to_use = combination(7, combo_colors)
    # 2. Uniquely assign these colors to the number of balls in combo
    dist = factorial(combo_colors) // \
           product(factorial(combo.count(color)) for color in set(combo))
    # 3. For each number, pick individual balls of a color to be used
    balls_colors = product(combination(10, color) for color in combo)

    s += balls_colors * dist  * colors_to_use * combo_colors

    print(combo, colors_to_use, dist, balls_colors)


o = combination(70, 20)
print(s, o, round(s/o, 9))