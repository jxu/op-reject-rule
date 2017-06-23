def proper_divisor_sum(n):
    s = 1  # Add 1 as a factor here
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            s += i
            if i != n//i: s += n//i
    return s

sums = [0] * 10**6
for i in range(10**6):
    sums[i] = proper_divisor_sum(i)

visited = [False]*10**6
max_chain = None
max_chain_len = 0

for i in range(10**6):
    if visited[i]: continue

    visited[i] = True
    seq = [i]
    valid_chain = True
    # Follow chain, marking as visited
    while sums[i] not in seq:
        i = sums[i]
        if i > 10**6:
            valid_chain = False
            break
        visited[i] = True
        seq.append(i)

    if valid_chain:
        chain = seq[seq.index(sums[i]):]  # Get cycle
        if len(chain) > max_chain_len:
            max_chain_len = len(chain)
            max_chain = chain

print(len(max_chain), max_chain)
print(min(max_chain))