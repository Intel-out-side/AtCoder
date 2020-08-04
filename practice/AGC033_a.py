#これだとTLEするっぽい
from collections import deque
H, W = list(map(int, input().split()))

city = []

for _ in range(H):
    city.append(list(input()))

black_grid = []

for i in range(H):
    for j in range(W):
        if city[i][j] == "#":
            black_grid.append((i, j))

dist = [[float("inf") for _ in range(W)] for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for start in black_grid:
    sx, sy = start
    queue = deque()
    queue.append(start)
    dist[sy][sx] = 0

    while len(queue) > 0:
        now_x, now_y = queue.popleft()

        for dx_, dy_ in zip(dx, dy):
            adj_x = now_x + dx_
            adj_y = now_y + dy_

            if (not 0 <= adj_x < W) or (not 0 <= adj_y < H):
                continue

            if city[adj_y][adj_x] == "#":
                continue

            #初めてそのマスに到達する場合
            if dist[adj_y][adj_x] > H*W:
                dist[adj_y][adj_x] = dist[now_y][now_x] + 1
                queue.append((adj_x, adj_y))

            elif H*W > dist[adj_y][adj_x] > dist[now_y][now_x] + 1:
                dist[adj_y][adj_x] = dist[now_y][now_x] + 1
                queue.append((adj_x, adj_y))


ans = -1
for i in range(H):
    for j in range(W):
        if dist[i][j] <= H*W:
            ans = max(dist[i][j], ans)

print(ans)
