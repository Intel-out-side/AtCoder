import sys
sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))

city = []

for i in range(H):
    city.append(list(input()))

visited = [[False for i in range(W)] for j in range(H)]

def dfs(i, j):
    if (not (0 <= i < H)) or (not (0 <= j < W)):
        return

    if visited[i][j]:
        return

    if city[i][j] == "#":
        return

    if city[i][j] == "g":
        print("Yes")
        sys.exit()

    if not visited[i][j]:
        visited[i][j] = True

    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i-1, j)
    dfs(i, j-1)

    return

start = None
for i in range(H):
    for j in range(W):
        if city[i][j] == "s":
            start = (i, j)


ans = dfs(start[0], start[1])
print("No")
