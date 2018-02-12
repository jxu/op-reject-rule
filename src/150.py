# Port of C answer (pypy 5.1.2: 4s, python3: 130s ??)
ROWS = 1000
row_prefix = [[0]*ROWS for i in range(ROWS)]

t = 0
for i in range(ROWS):
    for j in range(i+1):
        t = (615949*t + 797807) % 2**20
        row_prefix[i][j] = t - 2**19
        if (j > 0): row_prefix[i][j] += row_prefix[i][j-1]

min_tri = 0
for i in range(ROWS):
    for j in range(i+1):
        upper_tri_sum = 0
        for s in range(ROWS-i):
            upper_tri_sum += row_prefix[i+s][j+s]
            if (j > 0): upper_tri_sum -= row_prefix[i+s][j-1]
            min_tri = min(min_tri, upper_tri_sum)

print(min_tri)
