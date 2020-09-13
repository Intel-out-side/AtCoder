import heapq
N, M, T = map(int, input().split())
A = list(map(int, input().split()))

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

graphOut = [[] for _ in range(N)]
graphIn = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    graphOut[a-1].append(Edge(b-1, c))
    graphIn[b-1].append(Edge(a-1, c))

def dijkstraGo(start):
    dist = [float("inf") for i in range(N)]
    pq = []
    heapq.heapify(pq)

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for e in graphOut[now]:
            if dist[e.to] > dist[now] + e.cost:
                dist[e.to] = dist[now] + e.cost
                heapq.heappush(pq, (dist[e.to], e.to))
    return dist

def dijkstraBack(start):
    dist = [float("inf") for i in range(N)]
    pq = []
    heapq.heapify(pq)

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for e in graphIn[now]:
            if dist[e.to] > dist[now] + e.cost:
                dist[e.to] = dist[now] + e.cost
                heapq.heappush(pq, (dist[e.to], e.to))
    return dist

ans = -1
go = dijkstraGo(0)
back = dijkstraBack(0)
for i in range(N):
    ans = max(ans, (T - go[i] - back[i]) * A[i])


print(ans)
