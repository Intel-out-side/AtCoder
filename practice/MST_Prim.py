import heapq
N, M = map(int, input().split())

cost = [[0 for _ in range(N)] for _ in range(N)]

minCost = [float("inf") for _ in range(N)]
isUsed = [False for _ in range(N)]

def prim():
    minCost[0] = 0
    res = 0 #辺の重みの和
    pq = []
    heapq.heapify(pq)
    for i in range(N):
        if not isUsed[i]:
            heapq.heappush((i, minCost[i]))

    while True:
        #Xに属さない頂点の内からXからの辺のコストが最小になる頂点を探す
        v = -1
        for u in range(N):
            if not isUsed[u] and (v == -1 or minCost[u] < minCost[v]):
                v = u #未編入の頂点の内渡航コストが最小のもの

            # v = heapq.heappop(pq)

            if v == -1:
                break # すべて編入済ならbreak

            isUsed[v] = True # vは編入済

            res += minCost[v]

        for u in range(N):
            minCost[u] = min(minCost[u], cost[u][v])

    return res
