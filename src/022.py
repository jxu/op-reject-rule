names = open("p022_names.txt", 'r').read()
names = names.split(',')
names = sorted([name[1:-1] for name in names])

score = 0
for i in range(len(names)):
    score += (i+1) * sum(ord(c)-64 for c in names[i])
    
print(score)
