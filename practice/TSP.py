N = int(input()) #number of vertiles

N2 = 2**N #1 << N
dp = [[float("inf") for _ in range(N)] for _ in range(N2)]

dp[(1<<N)-1][0] = 0

#集合
for S in range((1<<N)-2, -1, -1):

    for v in range(N):
        for u in range(N):
            #uがまだ訪れていない頂点であるなら
            if not (S>>u & 1):
                dp[S][v] = min(dp[S][v], dp[S|1<<u][u] + dp[v][u])

ans = dp[0][0]
