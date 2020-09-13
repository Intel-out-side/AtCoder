import heapq
N, M, s, t = map(int, input().split())

class Edge:

    def __init__(self, to, yenCost, snukCost):
        self.to = to
        self.yenCost = yenCost
        self.snukCost = snukCost

graph = [[] for _ in range(N)]

for i in range(M):
    u, v, a, b = map(int, input().split())
    graph[u-1].append(Edge(v-1, a, b))
    graph[v-1].append(Edge(u-1, a, b))

moneyNow = 10**15

yenCost = [float("inf") for _ in range(N)]
snukCost = [float("inf") for _ in range(N)]

def dijkstra(start:int):
    pq = []
    heapq.heapify(pq)
    yenCost[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        d, v = heapq.heappop(pq)
        if d > yenCost[v]:
            continue
        for e in graph[v]:
            if yenCost[e.to] > yenCost[v] + e.yenCost:
                yenCost[e.to] = yenCost[v] + e.yenCost
                heapq.heappush(pq, (yenCost[e.to], e.to))

def dijkstra2(start:int):
    pq = []
    heapq.heapify(pq)
    snukCost[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        d, v = heapq.heappop(pq)
        if d > snukCost[v]:
            continue

        for e in graph[v]:
            if snukCost[e.to] > snukCost[v] + e.snukCost:
                snukCost[e.to] = snukCost[v] + e.snukCost
                heapq.heappush(pq, (snukCost[e.to], e.to))

dijkstra(s-1)
dijkstra2(t-1)
ans = 0
for mid in range(N):
    allCost = yenCost[mid] + snukCost[mid]
    print(moneyNow - allCost)
