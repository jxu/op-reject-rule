# Addition-chain exponentiation [NP-complete]
# No dynamic programming (not optimal substructure)
# No pruning: 115.4 s | Pruning: 20.9 s
import time
start_time = time.time()
m = [999 for i in range(201)]

def gen_tree(current_path, last):
    m[last] = min(m[last], len(current_path)-1)
    for n in current_path:
        # Tree max and depth limit, pruning
        if n + last <= 200 and len(current_path) <= 11 and len(current_path)-1 - m[last] <= 1:
            gen_tree(current_path + [n+last], n+last)

gen_tree([1], 1)
print(m)
print(sum(m[k] for k in range(1, 201)))
print(time.time() - start_time, 's')
