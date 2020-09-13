class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def getParent(self):
        return [self.find(i) for i in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if (root_x == root_y):
            return
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def memsInGroup(self, x):
        """
        O(N)かかります
        """
        root = self.find(x)
        return [i for i in range(N) if root == self.find(i)]

    def sizeOfGroup(self, x):
        return len(self.memsInGroup(x))


class Edge:

    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

H, W = map(int, input().split())
Sx, Sy = map(int, input().split())
Gx, Gy = map(int, input().split())

graph = [None] * H
for i in range(H):
    graph[i] = list(map(int, input().split()))

# import pprint
# pprint.pprint(graph)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

edges = []

for y in range(H):
    for x in range(W):
        for dx_, dy_ in zip(dx, dy):
            if (not 0 <= x + dx_ < W) or (not 0 <= y + dy_ < H):
                continue

            origin = W * y + x
            now = W * (y+dy_) + (x+dx_)
            score = graph[y][x] * graph[y+dy_][x+dx_]

            edges.append(Edge(origin, now, score))

edges.sort(reverse=True, key = lambda x: x.cost)
#最大全域木

res = 0
uf = UnionFind(H*W)
for e in edges:

    if not uf.isSame(e.u, e.v):
        res += e.cost
        uf.unite(e.u, e.v)

res += sum([sum(graph[i]) for i in range(H)])

print(res)
