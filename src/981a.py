from functools import cache
from more_itertools import distinct_permutations

# represent elements 1, -1, i, -i, j, -j, k, -k as 0 thru 7

MUL_TABLE = [
    [0, 1, 2, 3, 4, 5, 6, 7],  # 1
    [1, 0, 3, 2, 5, 4, 7, 6],  # -1
    [2, 3, 1, 0, 6, 7, 5, 4],  # i
    [3, 2, 0, 1, 7, 6, 4, 5],  # -i
    [4, 5, 7, 6, 1, 0, 2, 3],  # j
    [5, 4, 6, 7, 0, 1, 3, 2],  # -j
    [6, 7, 4, 5, 3, 2, 1, 0],  # k
    [7, 6, 5, 4, 2, 3, 0, 1],  # -k
]

# i^-1 = -i,  j^-1 = -j, k^-1 = -k
INV_TABLE = [0, 1, 3, 2, 5, 4, 7, 6]

PRINT_TABLE = ["1", "-1", "i", "-i", "j", "-j", "k", "-k"]
s = 0

for word in sorted(distinct_permutations([2,2,4,4,6,6])):
    
    x = 0
    for b in word:
        x = MUL_TABLE[x][b]

    if x == 0: s += 1

    print_word = ''.join(PRINT_TABLE[c] for c in word)

    print(print_word, PRINT_TABLE[x])

print(s)
