import heapq
class Edge:

    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

N, K = map(int, input().split())
graph = [[] for _ in range(N)]

def dijkstra(start, goal):
    dist = [float("inf") for _ in range(N)]
    dist[start] = 0

    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, start))

    while pq:
        cost, vertex = heapq.heappop(pq)

        if cost > dist[vertex]:
            continue

        for e in graph[vertex]:
            if dist[e.to] > dist[vertex] + e.cost:
                dist[e.to] = dist[vertex] + e.cost
                heapq.heappush(pq, (dist[e.to], e.to))

    return dist[goal]

for i in range(K):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, c, d, e = query
        graph[c-1].append(Edge(d-1, e))
        graph[d-1].append(Edge(c-1, e))

    else:
        _, a, b = query
        ans = dijkstra(a-1, b-1)

        if ans == float("inf"):
            print(-1)
        else:
            print(ans)
