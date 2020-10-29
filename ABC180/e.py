import heapq
N = int(input())
grid = []
edges = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    v = list(map(int, input().split()))
    grid.append(v)

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        a, b, c = grid[i]
        p, q, r = grid[j]

        edges[i][j] = abs(p-a) + abs(q-b) + max(0, r-c)

visited = [False] * N
mincost = [float("inf")]*N
mincost[0] = 0

res = 0
while True:
    v = -1
    for i in range(N):
        if not visited[i] and (v == -1 or mincost[i] < mincost[v]):
            v = i

    if v == -1:
        break

    visited[v] = True
    res += mincost[v]

    for i in range(N):
        mincost[i] = min(edges[v][i], mincost[i])

for i in range(1, N):
    visited = [False] * N
    mincost = [float("inf")]*N
    mincost[i] = 0
    while True:
        v = -1
        for i in range(N):
            if not visited[i] and (v == -1 or mincost[i] < mincost[v]):
                v = i

        if v == -1:
            break

        visited[v] = True
        res += mincost[v]

        for i in range(N):
            mincost[i] = min(edges[v][i], mincost[i])


print(res)
