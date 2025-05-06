from heapq import *

N = 10

a = [0]
b =[0]
s = 102022661
for n in range(1, 2*N+1):
    if n % 2: a.append(s)
    else: b.append(s)
    s = (s*s) % 998388889

print(a)
print(b)

def M(i,j):
    return a[i] + b[j]

# test Dijkstra's performance on small graphs
# priority queue elems are (priority, i, j) for M_ij
pq = [(M(1,1), 1, 1)]
visit = set()
n = 0

while True:
    n += 1
    node = heappop(pq)
    pri, i, j = node

    if (i,j) == (N,N): 
        print("done", pri)
        break 

    if i+1 <= N and (i+1,j) not in visit:
        visit.add((i+1,j))
        heappush(pq, (pri+M(i+1,j), i+1, j))

    if j+1 <= N and (i,j+1) not in visit:
        visit.add((i,j+1))
        heappush(pq, (pri+M(i,j+1), i, j+1))

    print(f"{n} {len(pq)} ({i},{j})")
    


