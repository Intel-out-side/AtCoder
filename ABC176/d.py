import pprint
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
edge = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    city.append(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[-1 for _ in range(W)] for _ in range(H)]
edgeList = []

def dfs(x, y, count):

    if (not (0 <= x < W)) or (not (0 <= y < H)):
        return

    if visited[y][x] > -1:
        return

    if x == Dw and y == Dh:
        visited[y][x] = count
        pprint.pprint(visited)
        print(count)
        exit()

    if city[y][x] == "#":
        for dx_, dy_ in zip(dx, dy):
            if visited[y+dy_][x+dx_] > -1:
                edgeList.append((x+dx_, y+dx_))
        return

    if visited[y][x] == -1:
        visited[y][x] = count

    dfs(x+1, y, count)
    dfs(x, y+1, count)
    dfs(x-1, y, count)
    dfs(x, y-1, count)

    for edge in edgeList:
        ex, ey = edge
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (not (0 <= ex+j < W)) or (not (0 <= ey+i < H)):
                    continue
                    if visited[ey+i][ex+j] > -1:
                        continue
                        if city[ey+i][ex+j] == "#":
                            continue

                            dfs(ex+j, ey+i, count+1)


dfs(Cw, Ch, 0)


print(visited[Dh][Dw])
