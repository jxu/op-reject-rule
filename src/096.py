# Backtracking's back (recursive solution)
import copy

grid_sum = 0

with open("p096_sudoku.txt", 'r') as f:
    lines = f.readlines()

def is_safe(grid, x, y, num):  # Beautiful isn't it
    sx, sy = x - x%3, y - y%3
    in_square = any(num in row[sx:sx+3] for row in grid[sy:sy+3])
    in_row = num in grid[y]
    in_col = num in [grid[i][x] for i in range(9)]

    return not in_square and not in_row and not in_col


def pretty_print(original_grid, grid, three_digit):
    for i in range(9):
        original_grid_row = ' '.join(str(a) for a in original_grid[i]).replace('0', '.')
        grid_row = ' '.join(str(a) for a in grid[i])
        print(original_grid_row + '\t\t\t' + grid_row)

    print("3-digit number: %s\n" % three_digit)


def solve_grid(grid, x, y):
    if 0 not in grid[8]:  # Solved
        return True, None

    # Move to next empty square
    while grid[y][x]:
        x += 1
        if x == 9:
            x = 0
            y += 1

    for num in range(1, 10):
        if is_safe(grid, x, y, num):
            grid[y][x] = num

            if (solve_grid(grid, x, y)[0]):  # Next solution is valid
                return True, grid

            grid[y][x] = 0  # Remove this solution

    return False, None  # Backtrack


for li in range(0, 500, 10):
    print(lines[li].rstrip())
    grid = [[int(b) for b in a.rstrip()] for a in lines[li+1:li+10]]
    original_grid = copy.deepcopy(grid)

    solved_grid = solve_grid(grid, 0, 0)[1]
    three_digit = 100*solved_grid[0][0] + 10*solved_grid[0][1] + solved_grid[0][2]
    grid_sum += three_digit
    pretty_print(original_grid, solved_grid, three_digit)

print("3-digit numbers sum: %s" % grid_sum)
