nums = []
for n in range(100):
    for e in range(2, 10):
        if n**e >= 10 and n == sum(int(c) for c in str(n**e)):
            nums.append(n**e)

print(sorted(nums)[29])
