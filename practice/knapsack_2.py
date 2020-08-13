N, W = list(map(int, input().split()))

value, weight = [0]*N, [0]*N

for i in range(N):
    v, w = list(map(int, input().split()))
    value[i], weight[i] = v, w

dp = [[float("inf") for _ in range(sum(value)+1)] for _ in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(sum(value)+1):
        if value[i] > j:
            dp[i+1][j] = dp[i][j]

        else:
            res1 = dp[i][j]
            res2 = dp[i][j - value[i]] + weight[i]

            dp[i+1][j] = min(res1, res2)


ans = 0
maxVal = -1
for i in range(len(dp[N])):

    if dp[N][i] <= W:
        maxVal = max(maxVal, dp[N][i])

ans = dp[N].index(maxVal)
print(ans)
