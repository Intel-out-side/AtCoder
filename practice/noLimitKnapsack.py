N, W = list(map(int, input().split()))

value, weight= [0]*N, [0]*N

for i in range(N):
    v, w = list(map(int, input().split()))
    value[i], weight[i] = v, w

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
"""
for i in range(N):
    for j in range(W+1):
        k = 0
        while k * weight[i] <= j:
            res1 = dp[i+1][j]
            res2 = dp[i][j - k*weight[i]] + k * value[i]
            dp[i+1][j] = max(res1, res2)
            k += 1
"""

for i in range(N):
    for j in range(W+1):
        if j < weight[i]:
            dp[i+1][j] = dp[i][j]
        else:
            res1 = dp[i][j]
            res2 = dp[i+1][j - weight[i]] + value[i]
            dp[i+1][j] = max(res1, res2)

print(dp[N][W])
