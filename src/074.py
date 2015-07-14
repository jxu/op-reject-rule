# Add chains if already seen
from math import factorial

def digit_factorial(n):
    return sum(map(lambda x: factorial(int(x)), str(n)))

chain_lens = [0]*10**7
for i in range(1000000):
    chain = [i]
    for j in range(60):
        next_num = digit_factorial(chain[-1])
        if next_num < 1000000 and chain_lens[next_num] != 0:
            chain_lens[i] = chain_lens[next_num] + len(chain)
            #print(chain, chain_lens[next_num], len(chain))

            break

        if next_num in chain:
            chain_lens[i] = len(chain)
            #print(chain, len(chain))
            break

        else:
            chain.append(next_num)

print(chain_lens[:1000000].count(60))




