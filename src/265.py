# De Bruijn sequences return...
# Generate strings using DFS, ignoring strings with "seen" subsequences

def S(arrange, seen, N):
    if len(arrange) == 2**N and 2*arrange.count(0) == 2**N:
        print(''.join(map(str, arrange)))
        return int(''.join(map(str, arrange)), 2)

    else:
        s = 0
        for c in (0, 1):
            new_seen = seen[:]
            new_arrange = arrange + [c]

            word = ''.join(map(str, new_arrange[-N:]))
            seen_i = int(word, 2)

            if not new_seen[seen_i]:
                new_seen[seen_i] = 1
                s += S(new_arrange, new_seen, N)

        return s


print(S([0]*5, [0]*2**5, 5))  # Beginning must be 00000 to remove rotations
