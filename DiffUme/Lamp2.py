H, W = map(int, input().split())

graph = []
for i in range(H):
    graph.append(input())

L = [[0 for _ in range(W)] for _ in range(H)]
U = [[0 for _ in range(W)] for _ in range(H)]
D = [[0 for _ in range(W)] for _ in range(H)]
R = [[0 for _ in range(W)] for _ in range(H)]


for y in range(H):
    for x in range(W):
        if graph[y][x] == "#":
            L[y][x] = 0
        elif x == 0:
            L[y][x] = 1
        else:
            L[y][x] = L[y][x-1] + 1

for x in range(W):
    for y in range(H):
        if graph[y][x] == "#":
            U[y][x] = 0
        elif y == 0:
            U[y][x] = 1
        else:
            U[y][x] = U[y-1][x] + 1

for x in range(W):
    for y in range(H-1, -1, -1):
        if graph[y][x] == "#":
            D[y][x] = 0
        elif y == H-1:
            D[y][x] = 1
        else:
            D[y][x] = D[y+1][x] + 1

for y in range(H):
    for x in range(W-1, -1, -1):
        if graph[y][x] == "#":
            R[y][x] = 0
        elif x == W-1:
            R[y][x] = 1
        else:
            R[y][x] = R[y][x+1] + 1

ans = -1
for y in range(H):
    for x in range(W):
        ans = max(ans, L[y][x] + R[y][x] + U[y][x] + D[y][x] - 3)

print(ans)
