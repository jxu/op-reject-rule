INF = 10**8
total_edge = 0

with open("p107_network.txt", 'r') as f:
    adj = f.read().split('\n')[:-1]
    for i in range(40):
        adj[i] = adj[i].split(',')
        adj[i] = [None if n == '-' else int(n) for n in adj[i]]
        total_edge += sum(n for n in adj[i] if n)


def min_key(key, mst):
    min_ = INF
    min_index = None

    for v in range(40):
        if not mst[v] and key[v] < min_:
            min_ = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    parent = [None]*40
    key = [INF]*40
    mst = [False]*40

    key[0] = 0
    parent[0] = -1

    for i in range(40-1):
        u = min_key(key, mst)
        mst[u] = True

        for v in range(40):
            if graph[u][v] and mst[v] == False and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    for i in range(1, 40):
        print(parent[i], i, graph[i][parent[i]])

    return key


print(total_edge - sum(prim_mst(adj)))










