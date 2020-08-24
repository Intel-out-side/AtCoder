import sys
sys.setrecursionlimit(10**8)
H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())

Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

city = []
for i in range(H):
    city.append(input())

visited = [[-1 for _ in range(W)] for _ in range(H)]

def dfs(x, y, count):

    if (not (0 <= x < W)) or (not (0 <= y < H)):
        return

    if visited[y][x] != -1:
        return

    if city[y][x] == "#":
        return

    if x == Dw and y == Ch:
        visited[y][x] = count
        return

    visited[y][x] = count
    dfs(x+1, y, count)
    dfs(x-1, y, count)
    dfs(x, y+1, count)
    dfs(x, y-1, count)

dfs(Cw, Ch, 0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for x in range(W):
    for y in range(H):
        for dx_, dy_ in zip(dx, dy):
            if city[y+dy





import pprint
pprint.pprint(visited)
ans = visited[Dh][Dw]
print(ans)
