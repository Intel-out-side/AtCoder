H, W = map(int, input().split())

graph = []
for i in range(H):
    s = input()
    graph.append(s)


def dfs(now, increment, count):
    now = (now[0] + increment[0], now[1] + increment[1])
    x, y = now

    if (not 0 <= x < W) or (not 0 <= y < H):
        return count - 1

    if graph[y][x] == "#":
        return count - 1

    if count == 5:
        return 4

    return dfs(now, increment, count+1)

ans = 1
for y in range(H):
    for x in range(W):
        if graph[y][x] == '.':
            a = dfs((x, y), (0, 1), 1)
            b = dfs((x, y), (0, -1), 1)
            c = dfs((x, y), (1, 0), 1)
            d = dfs((x, y), (-1, 0), 1)
            ans = max(ans, 1 + a + b + c + d)

print(ans)
