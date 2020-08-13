N, M = None, None

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(N+1):
        if i - j >= 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % M
        else:
            dp[i][j] = dp[i-1][j]
