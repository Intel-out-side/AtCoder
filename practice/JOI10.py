from collections import deque
from pprint import pprint
H, W, N = list(map(int, input().split()))

city = []
for _ in range(H):
    city.append(list(input()))

#スタートの座標
sx, sy = 0, 0
for i in range(H):
    for j in range(W):
        if city[i][j] == "S":
            sy, sx = i, j

ans = 0
for i in range(1, N+1):
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]

    queue = deque()
    queue.append((sx, sy))

    dist[sy][sx] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #i個目に食べるべきチーズ
    gx, gy = sx, sy

    while len(queue) != 0:
        now_x, now_y = queue.popleft()

        for dx_, dy_ in zip(dx, dy):
            adj_x, adj_y = now_x + dx_, now_y + dy_

            if (not 0<= adj_x < W) or (not 0<=adj_y<H):
                continue

            if city[adj_y][adj_x] == "X":
                continue

            if city[adj_y][adj_x] == str(i):
                gx, gy = adj_x, adj_y

            if dist[adj_y][adj_x] > H*W:
                dist[adj_y][adj_x] = dist[now_y][now_x] + 1
                queue.append((adj_x, adj_y))

    ans += dist[gy][gx]
    sx, sy = gx, gy


print(ans)
