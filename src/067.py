# Same as 18
t = open("p067_triangle.txt", 'r').read()
t = [r.split(' ') for r in t.split('\n')]
t = [[int(n) for n in r] for r in t[:-1]]

for i in range(1, len(t)):
    t[i][0] += t[i-1][0]
    t[i][i] += t[i-1][i-1]
    for j in range(1,i):
        t[i][j] += max(t[i-1][j-1], t[i-1][j]) 

print(max(t[-1]))


