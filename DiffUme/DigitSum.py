K = input()
D = int(input())

N = len(K)

MOD = 10**9 + 7

dp = [[[0 for _ in range(2)] for _ in range(D)] for _ in range(N+1)]
#dp[i桁目のdigitを見る][ここまでの余りの合計][1:K以下であることが確定、0:未確定(i桁目まで一致)]

for d in range(10):
    digit = int(K[0])
    if d > digit: continue

    if d == digit:
        dp[1][d%D][0] += 1

    if d < digit:
        dp[1][d%D][1] += 1

for i in range(1, N):
    for r in range(D):
        for k in range(2):

            ithDigit = int(K[i])

            for d in range(10):
                ni, nr, nk = i+1, (r+d)%D, k

                if k == 0:
                    if d > ithDigit: continue
                    if d < ithDigit: nk = 1

                dp[ni][nr][nk] += dp[i][r][k]
                dp[ni][nr][nk] %= MOD

# print(dp)
ans = dp[N][0][1] + dp[N][0][0] - 1
print(ans)
