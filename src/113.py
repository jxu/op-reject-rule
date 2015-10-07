# Not bouncy = increasing, decreasing, or straight
# Increasing can start with 0, decreasing can't
pow_10 = 100
decreasing = [[0]*10 for i in range(pow_10)]
decreasing[0] = [1]*10

for i in range(1, pow_10):
    for j in range(10):
        decreasing[i][j] = sum(decreasing[i-1][:j+1])

total_sum = 0
for i in decreasing:
    print(i, sum(i))
    total_sum += sum(i)

total_sum += sum(decreasing[-1])  # Increasing
final = total_sum - 10*pow_10 - 1  # Magic adjustment factor

print(final)
