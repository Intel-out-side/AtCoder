class UnionFind():

    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

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

N, Q = map(int, input().split())

unionFind = UnionFind(N)

for i in range(Q):
    p, a, b = map(int, input().split())
    # print(unionFind.membersInSameGroup(a-1))

    if p == 0:
        unionFind.unite(a-1, b-1)
    elif p == 1:
        if unionFind.isSame(a-1, b-1):
            print("Yes")
        else:
            print("No")
