from collections import defaultdict, deque
import heapq
N, M = map(int, input().split())

graph = defaultdict(list)
indeg = defaultdict(int)

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    indeg[b] += 1

q = []
for i in range(N):
    if indeg[i] == 0:
        q.append(i)

heapq.heapify(q)
ans = []
while q:
    now = heapq.heappop(q)
    ans.append(now)
    for adj in graph[now]:
        indeg[adj] -= 1

        if indeg[adj] == 0:
            heapq.heappush(q, adj)
if len(ans) == N:
    for i in range(N):
        ans[i] += 1
    print(*ans)
else:
    print(-1)