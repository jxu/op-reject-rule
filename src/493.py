# Monte Carlo method (incomplete)
import random
trials = 100000

urn = list(range(7)) * 10
total = 0
for i in range(trials):
    choice = random.sample(urn, 20)
    total += len(set(choice))
    
print('%.10f' % (total / trials))