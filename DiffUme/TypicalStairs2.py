N, M = map(int, input().split())
isBroken = [0] * (N+1)

for i in range(M):
    a = int(input())
    isBroken[a] = 1

dp = [0 for _ in range(N+2)]
#幻のN+1段目まで生やして、そこの組み合わせをゼロにする

dp[N] = 1
for i in range(N-1, -1, -1):
    if isBroken[i]:
        dp[i] = 0
        continue
    dp[i] = dp[i+1] + dp[i+2]
print(dp[0] % (10**9 + 7))
