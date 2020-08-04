from collections import deque
from pprint import pprint

H, W = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

sx -= 1
sy -= 1
gy -= 1
gx -= 1

maze = []

for _ in range(H):
    maze.append(list(input()))

dist = [[float("inf") for _ in range(W)] for _ in range(H)]

queue = deque()

queue.append((sx, sy))
dist[sy][sx] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while len(queue) != 0:
    now_x, now_y = queue.popleft()
    for dx_, dy_ in zip(dx, dy):

        adj_x = now_x + dx_
        adj_y = now_y + dy_
        if (not 0<=adj_x<W) or (not 0<=adj_y<H):
            continue

        if maze[adj_y][adj_x] == "#":
            continue

        if dist[adj_y][adj_x] >= H*W:
            dist[adj_y][adj_x] = dist[now_y][now_x] + 1
            queue.append((adj_x, adj_y))

print(dist[gy][gx])
