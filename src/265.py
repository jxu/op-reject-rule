# De Bruijn sequences return...
# Generate strings using DFS, ignoring strings with "seen" subsequences

candidates = []
N = 5
s = 0

def S(arrange, seen):
    global candidates, s

    if len(arrange) == 2**N and 2*arrange.count(0) == 2**N:
        print(''.join(map(str, arrange)))
        s += int(''.join(map(str, arrange)), 2)

    else:
        for c in (0, 1):
            new_seen = seen[:]
            new_arrange = arrange + [c]

            if len(new_arrange) <= N and c == 1:  # Beginning must be 00000 to remove rotations
                continue

            if len(new_arrange) >= N:
                word = ''.join(map(str, new_arrange[-N:]))
                seen_i = int(word, 2)

                if not new_seen[seen_i]:
                    new_seen[seen_i] = 1
                    S(new_arrange, new_seen)

            else:
                S(new_arrange, new_seen)


S([], [0]*2**N)
print(s)
