N = int(input())
p = list(map(int, input().split()))
maxPoint = sum(p)

dp = [[0 for _ in range(maxPoint+1)] for _ in range(N+1)]

dp[0][0] = 1  # ゼロ個の整数の和＝０なのでTrue

for i in range(N):
    for j in range(maxPoint+1):

        if maxPoint < p[i]:
            dp[i+1][j] = dp[i][j]

        else:
            dp[i+1][j] = dp[i][j] or dp[i][j - p[i]]

print(dp[N].count(1))
