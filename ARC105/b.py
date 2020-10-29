from collections import defaultdict
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


N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dif = [b[i]-a[i] for i in range(N)]

uf = UnionFind(N)

for i in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    uf.unite(c, d)

count = defaultdict(int)
for i in range(N):
    count[uf.find(i)] += dif[i]

allZero = True
for vals in count.values():
    if vals != 0:
        allZero = False

if allZero:
    print("Yes")
else:
    print("No")
