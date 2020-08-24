from collections import deque
N, Q = map(int, input().split())

graph = [[] for i in range(N)]

score = [0 for _ in range(N)]
"""
def dfs(now, prev, addVal, visited):
    if graph[now] == prev:
        score[now]+= addVal
        return

    score[now] += addVal

    for adj in graph[now]:
        if adj < now:
            continue
        if adj == prev:
            continue
        if visited[adj]:
            continue
        visited[adj] = True

        dfs(adj, now, addVal, visited)
"""

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(Q):
    p, x = map(int, input().split())

    visited = [False for _ in range(N)]
    queue = deque()
    queue.append(p-1)
    score[p-1] += x

    while queue:
        now = queue.popleft()

        for adj in graph[now]:
            if adj < now or visited[adj]:
                continue
            score[adj] += x
            visited[adj] = True
            queue.append(adj)

for i in range(N):
    print(score[i])
