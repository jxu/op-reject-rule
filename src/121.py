from itertools import combinations
from math import factorial

total_red = 0
for reds in range(0, 8):
    for combo in combinations(range(1, 16), reds):
        product = 1
        for n in combo: product *= n
        total_red += product

print(int(factorial(16) / total_red))  # 16! = total ways
