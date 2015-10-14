# Addition-chain exponentiation [NP-complete]
# No dynamic programming (not optimal substructure)
# No pruning: 115.4 s | Pruning: 20.9 s | mult_count and more pruning: 1.1 s
import time
start_time = time.time()
m = [999 for i in range(201)]

def gen_tree(current_path, last, mult_count):
    m[last] = min(m[last], mult_count)
    for n in current_path:
        # Tree max, tree depth limit, pruning
        if n + last <= 200 and mult_count <= 10 and mult_count - m[last] <= 0:
            gen_tree(current_path + [n+last], n+last, mult_count+1)

gen_tree([1], 1, 0)
print(m)
print(sum(m[k] for k in range(1, 201)))
print(time.time() - start_time, 's')
