N = int(input())
A = list(map(int, input().split()))

K = 10

MOD = 998244353

dp = [[0 for _ in range(K)] for _ in range(N)]

dp[0][A[0]] = 1

for i in range(N-1):
    for k in range(K):
        dp[i+1][(k+A[i+1])%10] += dp[i][k]%MOD
        dp[i+1][(k+A[i+1])%10] %= MOD
        dp[i+1][(k*A[i+1])%10] += dp[i][k]%MOD
        dp[i+1][(k*A[i+1])%10] %= MOD

for k in range(K):
    print(dp[N-1][k]%MOD)