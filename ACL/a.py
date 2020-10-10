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

if __name__ == "__main__":
    N, Q = map(int, input().split())
    test = UnionFind(N)

    for i in range(Q):
        query = list(map(int, input().split()))
        u, v = query[1], query[2]
        if query[0] == 0:
            test.unite(u-1, v-1)
        else:
            isSame = test.isSame(u-1, v-1)
            if isSame:
                print(1)
            else:
                print(0)
