#ダイクストラ法：負コストの経路が存在しない場合の最短経路を求める

import heapq
N = int(input()) #頂点の数
dist = [float("inf") for _ in range(N)] #距離
isUsed = [False for _ in range(N)] #すでに最短距離が確定したかどうか

def dijkstra(start:int):
    dist[start] = 0
    while True:
        v = -1
        for u in range(N):
            if not isUsed[u] and (v == -1 or dist[u] < dist[v]):
                v = u

        if v == -1:
            #すべての頂点の距離が確定したらブレーク
            break

        isUsed[v] = True
        for u in range(N):
            dist[u] = min(dist[u], dist[v] + cost[u][v])

class Edge:

    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

V = 100 # num of edges
G = [edge(0, 0) for _ in range(N)]
dist = [float("inf") for _ in range(N)]

def dijkstra(start):
    pq = [] #最短距離と頂点番号を入れる
    heapq.heapify(pq)
    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, v = heapq.heappop(pq)
        if dist[v] < cost:
            continue
        for e in G[v]:
            if dist[e.to] > dist[v] + e.cost:
                dist[e.to] = dist[v] + e.cost
                heapq.heappush((dist[e.to], e.to))
