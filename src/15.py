# Grid solution
grid = [[0]*21 for i in range(21)]
grid[0][0] = 1

for i in range(21):
    for j in range(21):
        if i >= 1: grid[i][j] += grid[i-1][j]
        if j >= 1: grid[i][j] += grid[i][j-1]
        
print(grid[20][20])


# Pascal's triangle solution: 1, 2, 6, ...
# 40 C 20
import math
print(math.factorial(40)/math.factorial(20)**2)


        