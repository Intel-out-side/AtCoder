from collections import deque
H, W = map(int, input().split())

graph = []
for i in range(H):
    s = input()
    graph.append(s)

s, g = None, None
for y in range(H):
    for x in range(W):
        if graph[y][x] == "s":
            s = (x, y)
        if graph[y][x] == "g":
            g = (x, y)

        if s is not None and g is not None:
            break

dist = [[float("inf") for _ in range(W)] for _ in range(H)]

dq = deque()
dq.append(s)
dist[s[1]][s[0]] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while dq:
    x, y = dq.popleft()

    for dx_, dy_ in zip(dx, dy):
        if (not 0 <= x + dx_ < W) or (not 0 <= y + dy_ < H):
            continue

        if (graph[y+dy_][x+dx_] == "." or graph[y+dy_][x+dx_] == "g") and dist[y+dy_][x+dx_] > dist[y][x]:
            dist[y+dy_][x+dx_] = dist[y][x]
            dq.appendleft((x+dx_, y+dy_))

    for dx_, dy_ in zip(dx, dy):
        if (not 0 <= x + dx_ < W) or (not 0 <= y + dy_ < H):
            continue

        if graph[y+dy_][x+dx_] == "#" and dist[y+dy_][x+dx_] == float("inf"):
            dist[y+dy_][x+dx_] = dist[y][x] + 1
            dq.append((x+dx_, y+dy_))

gx, gy = g
if dist[gy][gx] <= 2:
    print("YES")
else:
    print("NO")
