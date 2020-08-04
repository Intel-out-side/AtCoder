from collections import deque
H, W = list(map(int, input().split()))

g = []

for _ in range(H):
    g.append(list(input()))

dist = [[-1 for _ in range(W)] for _ in range(H)]
queue = deque()

for i in range(H):
    for j in range(W):
        if g[i][j] == "#":
            dist[i][j] = 0
            queue.append((j, i))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while len(queue) > 0:
    now_x, now_y = queue.popleft()

    for dx_, dy_ in zip(dx, dy):
        adj_x = now_x + dx_
        adj_y = now_y + dy_

        if (not 0 <= adj_x < W) or (not 0 <= adj_y < H):
            continue

        if g[adj_y][adj_x] == "#" :
            continue

        if g[adj_y][adj_x] == ".":
            g[adj_y][adj_x] = "#"
            queue.append((adj_x, adj_y))
            dist[adj_y][adj_x] = dist[now_y][now_x] + 1

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(dist[i][j], ans)

print(ans)
