from itertools import combinations

squares = ((0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1))

def digits_on_cubes(digit1, digit2, cube1, cube2):
    return (digit1 in cube1 and digit2 in cube2) or \
           (digit2 in cube1 and digit1 in cube2)


def all_digits_on_cubes(cube1, cube2):
    # Extend set if necessary
    if 6 in cube1: cube1 = cube1 + (9,)
    if 9 in cube1: cube1 = cube1 + (6,)
    if 6 in cube2: cube2 = cube2 + (9,)
    if 9 in cube2: cube2 = cube2 + (6,)

    return all(digits_on_cubes(d1, d2, cube1, cube2) for d1, d2 in squares)


count = 0
for cube1 in combinations(range(10), 6):
    for cube2 in combinations(range(10), 6):
        if all_digits_on_cubes(cube1, cube2):
            print(cube1, cube2)
            count += 1


print(count//2)  # Each pair is counted twice (order)