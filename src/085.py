# Rectangles defined by 2 horizontal and 2 vertical lines (n+1, m+1 choose 2)
# ((n+1)n/2) * ((m+1)m/2) = 2000000
min_dif = 100000
area = None
for m in range(3000):
    for n in range(m):
        if abs((n+1)*n * (m+1)*m - 8000000) < min_dif:
            min_dif = abs((n+1)*n * (m+1)*m - 8000000)
            area = n*m

print(area)