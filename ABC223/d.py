from collections import defaultdict, deque
N, M = map(int, input().split())

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

edges = defaultdict(list)
deg = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    deg[b] += 1
    edges[a].append(b)

isVisited = [0 for i in range(N+1)]

ans = ""
isImpossible = False

def dfs(par, now):
    global ans
    global isImpossible
    ans += str(now)

    for adj in edges[now]:
        if isVisited[adj]:
            isImpossible = True
            continue
        dfs(par, adj)

#閉路検出
for i in range(1, N+1):
    isVisited = [False for _ in range(N+1)]
    dfs(i, i)

if isImpossible:
    print(-1)
    exit()


ans = list(v for v in range(1, N+1) if deg[v]==0)
deq = deque(ans)
used = [0]*N

while deq:
    v = deq.popleft()
    for t in edges[v]:
        deg[t] -= 1
        if deg[t]==0:
            deq.append(t)
            ans.append(t)

print(ans)