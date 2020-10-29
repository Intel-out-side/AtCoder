#traveling salesman problem

N = int(input())
grid = [0]*N
for i in range(N):
    grid[i] = tuple(map(int, input().split()))

dist = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a, b, c = grid[i]
        p, q, r = grid[j]
        dist[i][j] = abs(p-a) + abs(q-b) + max(0, r-c)

dp = [[float("inf") for _ in range(N)] for _ in range(1<<N)]
dp[1][0] = 0

for S in range(1<<N):

    for now in range(N):
        for nxt in range(N):
            if (S>>nxt)&1: continue

            dp[S|(1<<nxt)][nxt] = min(dp[S|(1<<nxt)][nxt], dp[S][now] + dist[now][nxt])

ans = min(dp[(1<<N)-1][i] + dist[i][0] for i in range(N))

print(ans)
