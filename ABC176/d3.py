from collections import deque
H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
Ch -= 1; Cw -= 1; Dh -= 1; Dw -= 1;
S = []

for _ in range(H):
    S.append(input())

dq = deque()
dq.append((Cw, Ch))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[-1 for _ in range(W)] for _ in range(H)]
visited[Ch][Cw] = 0
while dq:
    x, y = dq.popleft()

    #コスト無しで行けるエリアを列挙
    for dx_, dy_ in zip(dx, dy):
        if (not 0 <= x+dx_ < W) or (not 0 <= y+dy_ < H):
            continue
        if S[y+dy_][x+dx_] == "#":
            continue
        #まだ訪れていない or 実はノーコストで到達可能な点だった
        if visited[y+dy_][x+dx_] == -1 or visited[y+dy_][x+dx_] > visited[y][x]:
            visited[y+dy_][x+dx_] = visited[y][x]
            dq.appendleft((x+dx_, y+dy_))

    for i in range(-2, 3):
        for j in range(-2, 3):
            if (not 0 <= x+i < W) or (not 0 <= y+j < H):
                continue
            if S[y+j][x+i] == '#':
                continue

            if visited[y+j][x+i] == -1:
                visited[y+j][x+i] = visited[y][x] + 1
                dq.append((x+i, y+j))

ans = visited[Dh][Dw]
print(ans)
