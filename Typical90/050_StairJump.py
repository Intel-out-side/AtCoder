N, L = map(int, input().split())

dp = [0 for _ in range(N+1)]

dp[0] = 1

for i in range(N+1):
    if not (i+1 > N):
        dp[i+1] += dp[i]

    if not(i+L > N):
        dp[i+L] += dp[i]

print(dp[N]%(10**9+7))