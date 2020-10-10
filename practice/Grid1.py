import pprint
H, W = map(int, input().split())
grid = [0] * H
MOD = 10**9 + 7

for i in range(H):
    s = input()
    grid[i] = s
# pprint.pprint(grid)


dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for y in range(H):
    for x in range(W):

        for dx_, dy_ in zip(dx, dy):

            if not 0 <= x+dx_ < W or not 0 <= y + dy_ < H:
                continue

            if grid[y+dy_][x+dx_] == "#":
                continue

            dp[y+dy_][x+dx_] += dp[y][x]
            dp[y+dy_][x+dx_] %= MOD

# pprint.pprint(dp)
ans = dp[H-1][W-1]
print(ans)
