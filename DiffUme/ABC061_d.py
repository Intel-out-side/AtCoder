class Edge:
    def __init__(self, f, to, cost):
        self.to = to
        self.origin = f
        self.cost = cost

N, M = map(int, input().split())

edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append(Edge(a-1, b-1, c))

dist = [-float("inf") for _ in range(N)]
dist[0] = 0
i = 0
while True:
    isUpdated = False
    for e in edges:
        if dist[e.origin] != -float("inf") and dist[e.to] < dist[e.origin] + e.cost:
            dist[e.to] = dist[e.origin] + e.cost
            isUpdated = True
    # print(dist)
    i += 1

    if not isUpdated:
        break

    if i == N-2:
        break

positive = [0 for _ in range(N)]
def findInfLoop():
    for i in range(N):
        for e in edges:
            if dist[e.origin] != -float("inf") and dist[e.to] < dist[e.origin] + e.cost:
                dist[e.to] = dist[e.origin] + e.cost
                positive[e.to] = 1

if positive[N-1]:
    print("inf")
else:
    print(dist[N-1])
