import sys
from collections import deque
sys.setrecursionlimit(10**7)
#累積和を木に拡張する
N, Q = map(int, input().split())

graph = [[] for i in range(N)]
score = [0 for _ in range(N)]

def dfs(now, prev):

    for adj in graph[now]:
        if adj == prev:
            continue
        score[adj] += score[now]
        dfs(adj, now)

    return

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

query = [0] * N
for i in range(Q):
    p, x = map(int, input().split())

    score[p-1] += x

dfs(0, -1)

for p in score:
    print(p)
