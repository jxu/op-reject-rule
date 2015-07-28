# Prim's algorithm
total_edge = 0

with open("p107_network.txt", 'r') as f:
    adj = f.read().split('\n')[:-1]
    for i in range(40):
        adj[i] = adj[i].split(',')
        adj[i] = [None if n == '-' else int(n) for n in adj[i]]
        total_edge += sum(n for n in adj[i] if n)  # Each edge counted twice

T = set()
X = set([0])  # Starting point

while len(X) != 40:
    crossing = set()

    for x in X:
        for k in range(40):
            if k not in X and adj[x][k]:
                crossing.add((x, k))

    edge = sorted(crossing, key=lambda e: adj[e[0]][e[1]])[0]
    T.add(edge)
    X.add(edge[1])


min_weight = sum(adj[e[0]][e[1]] for e in T)
print(total_edge//2 - min_weight)
