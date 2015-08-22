# Occult pentagram
# Numbering clockwise: outside, inside (join_order)
from itertools import permutations

all_seq = permutations(list(range(1, 11)), 10)

def seq_sum(seq, a, b, c):
    return seq[a] + seq[b] + seq[c]

max_str = []
for seq in all_seq:
    target_sum = seq_sum(seq, 0, 1, 3)
    
    if seq[0] == min(seq[0], seq[2], seq[4], seq[6], seq[8]) and \
    target_sum == seq_sum(seq, 2, 3, 5) == seq_sum(seq, 4, 5, 7) == seq_sum(seq, 6, 7, 9) == seq_sum(seq, 8, 9, 1):
        join_order = (0, 1, 3, 2, 3, 5, 4, 5, 7, 6, 7, 9, 8, 9, 1)
        s = ""
        for i in range(len(join_order)):
            s += str(seq[join_order[i]])
            
        if len(s) == 16:
            max_str += [int(s)]
            
print(max(max_str))
