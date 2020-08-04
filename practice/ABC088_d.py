from collections import deque
import sys
H, W = list(map(int, input().split()))

city = []

for _ in range(H):
    city.append(list(input()))

dist = [[float("inf") for _ in range(W)] for _ in range(H)]

dist_count = [0 for _ in range(H*W)]

queue = deque()
queue.append((0, 0))
dist[0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while len(queue) > 0:
    now_x, now_y = queue.popleft()

    for dx_, dy_ in zip(dx, dy):

        adj_x = now_x + dx_
        adj_y = now_y + dy_

        if (not 0 <= adj_x < W) or (not 0 <= adj_y < H):
            continue

        if city[adj_y][adj_x] == "#":
            continue

        if dist[adj_y][adj_x] > H*W:
            dist[adj_y][adj_x] = dist[now_y][now_x] + 1
            queue.append((adj_x, adj_y))
            dist_count[dist[adj_y][adj_x]] += 1

#すぬけ君がどうやってもたどり着けない場合
if dist[H-1][W-1] > H**W:
    print(-1)
    sys.exit()

#すぬけ君がたどり着ける場合
route_grids = dist[H-1][W-1] + 1

white_all = 0
for i in range(H):
    for j in range(W):
        if city[i][j] == ".":
            white_all += 1
ans = white_all - route_grids
print(ans)
