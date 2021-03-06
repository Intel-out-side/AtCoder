"""
クラスカル法による最小(最大)全域木を求めるコードです。
O(|E|log|E|)≒O(|E|log|V|)です
"""

V, E = map(int, input().split())
edges = [None] * E

class UnionFind:
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

for i in range(E):
    v1, v2, cost = map(int, input().split())
    edges[i] = Edge(v1, v2, cost)
    #edges[i] = Edge(v1-1, v2-1, cost)

edges.sort(key = lambda x:x.cost)
#最大全域木なら reverse = Trueにする

def kruskal():
    uf = UnionFind(V)
    res = 0

    for e in edges:
        if not uf.isSame(e.u, e.v):
            uf.unite(e.u, e.v)
            res += e.cost

    return res

print(kruskal())
