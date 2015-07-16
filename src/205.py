import itertools

peter = [0]*37
colin = [0]*37
for roll in itertools.product((1, 2, 3, 4), repeat=9):
    peter[sum(roll)] += 1

for roll in itertools.product((1, 2, 3, 4, 5, 6), repeat=6):
    colin[sum(roll)] += 1

peter_win = 0
for i in range(37):
    peter_win += sum(colin[:i]) * peter[i]

total = sum(peter) * sum(colin)
print(round(peter_win / total, 7))
