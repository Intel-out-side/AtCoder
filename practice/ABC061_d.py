class Edge:

    def __init__(self, origin, to, cost):
        self.origin = origin
        self.to = to
        self.cost = cost

N, M = map(int, input().split())

edges = [None] * M

for i in range(M):
    a, b, c = map(int, input().split())
    edges[i] = Edge(a-1, b-1, -c)

#コストを最小化するような問題として読み替える

dist = [float("inf") for _ in range(N)]
dist[0] = 0
i = 0
while True:
    isUpdated = False
    for e in edges:
        if dist[e.origin] != float("inf") and dist[e.to] > dist[e.origin] + e.cost:
            dist[e.to] = dist[e.origin] + e.cost
            isUpdated = True
    i += 1

    if not isUpdated:
        break

    if i == N-1:
        break

# print(dist)

#最短経路探索が終了
#負のサイクルを検知する
isUpdated = [False for _ in range(N)]
for i in range(N):
    for e in edges:
        if dist[e.to] > dist[e.origin] + e.cost:
            dist[e.to] = dist[e.origin] + e.cost
            isUpdated[e.to] = True


if isUpdated[N-1]:
    print("inf")

else:
    print(-dist[N-1])
