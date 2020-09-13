#Bellman-Ford
#経路に負のコストの辺が含まれるような場合に使えるっぽい
#負のコストの辺を検出することができるっぽい
N, M = map(int, input().split())

class Edge:

    def __init__(self):
        self.from = 0
        self.to = 0
        self.cost = 0

edges = [Edge() for _ in range(N)]

def BellmanFord(start:int):
    dist = [float("inf") for _ in range(N)]
    d[start] = 0

    while True:
        isUpdated = False
        for i in range(E):
            e = edges[i]
            #すでに更新された頂点から
            if d[e.from] != float("inf") and d[e.to] > d[e.from] + e.cost:
                d[e.to] = d[e.from] + e.cost
                isUpdated = True

        if not isUpdated:
            break
