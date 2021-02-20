N, K = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1

acum = [0] * (K+1)

for i in range(N):
    a
    for j in range(K+1):
        acum[j] += dp[i][j]

    for j in range(K+1):
        dp[i+1][j] += acum[j - a[i]] - acum[0]
        dp[i+1][j] %= MOD
ans = dp[N][K]
print(ans)
