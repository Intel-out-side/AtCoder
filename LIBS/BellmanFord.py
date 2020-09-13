"""
ベルマンフォード法です。
辺のコストがバラバラ＆負のコストが存在する場合使います。
O(|V|+|E|)でできます。
"""

class Edge:

    def __init__(self, origin, to, cost):
        self.origin = origin
        self.to = to
        self.cost = cost


# N: 頂点の数　　M:辺の数
N, M = map(int, input().split())

# すべての辺
edges = [None] * M

for i in range(M):
    a, b, c = map(int, input().split())
    edges[i] = Edge(a-1, b-1, c)

    #無向グラフなら下をアンコメントする
    # edges[i] = Edge(b-1, a-1, c)

dist = [float("inf") for _ in range(N)]
# start = 0
dist[start] = 0

i = 0
while True:
    isUpdated = False
    for e in edges:
        # originが更新済み　なら　originと隣接する頂点との距離を更新する
        if dist[e.origin] != float("float") and dist[e.to] > dist[e.origin] + e.cost:
            dist[e.to] = dist[e.origin] + e.cost
            isUpdated = True

    i += 1
    if not isUpdated: #もしN-1回目までに更新が終わる　-> 負の閉路無し
        break

    if i == N-1:　#もしN回目も更新がある -> 負の閉路がある
        break
