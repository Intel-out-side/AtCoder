from collections import deque
N, X, Y = map(int, input().split())

pairs = [set() for _ in range(N)]

graph = [[] for _ in range(N)]
for i in range(N-1):
    graph[i].append(i+1)
    graph[i+1].append(i)

graph[X-1].append(Y-1)
graph[Y-1].append(X-1)

distCount = [0 for _ in range(N)]

for i in range(N):

    dist = [0 for _ in range(N)]
    visited = [False for _ in range(N)]
    queue = deque()
    queue.append(i)
    visited[i] = True

    #bfs
    while len(queue) > 0:
        now = queue.popleft()
        for adj in graph[now]:
            if visited[adj]:
                continue
            queue.append(adj)
            dist[adj] = dist[now] + 1
            #countでやるんじゃなくてdist[now] + 1でやるとミスがない
            visited[adj] = True


    for j in range(N):
        distCount[dist[j]] += 1

for i in range(1, N):
    print(distCount[i]//2)
