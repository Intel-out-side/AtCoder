N, K = map(int, input().split())
a = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1

acum = [0 for _ in range(K+1)]

for i in range(1, N+1):
    acum[0] = 0
    for j in range(1, K+1):
        #j : i人目までにj個配れるアメが存在する
        acum[j] = (acum[j-1] + dp[i-1][j-1])%MOD

    for j in range(K+1):
        dp[i][j] = (acum[j+1] - acum[max(0, j-a[i])] + MOD)%MOD
    
