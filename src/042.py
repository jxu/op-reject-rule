words = open("p042_words.txt", 'r').read().split(',')

triangle_nums = set(n*(n+1)//2 for n in range(100))
s = 0
for word in words:
    if sum(ord(c)-64 for c in word[1:-1]) in triangle_nums: s += 1

print(s)
