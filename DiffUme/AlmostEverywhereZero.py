N = int(input())
K = int(input())

S = str(N)
D = len(S)

#dp[i桁目まで決めたとき][smaller == 1でそれ未満、==0で以上]
dp = [[[0]*2 for _ in range(K+1)] for _ in range(D+5)]
dp[0][0][0] = 1

# i :i桁目まで決めた時
# j :j個の非ゼロ整数がすでにある
# k :0 -> N以下であると確定していない(i桁目までは一致), 1->otherwise

for i in range(D):
    for j in range(4):
        for k in range(2):

            ithDigit = int(S[i])

            for d in range(10):
                ni, nj, nk = i+1, j, k

                if d != 0:
                    nj += 1
                if nj > K:
                    continue

                #N以下であることが確定していない(i桁目までは一致)
                if k == 0:
                    if d > ithDigit:
                        #continue
                        pass
                    if d < ithDigit:
                        nk = 1

                dp[ni][nj][nk] += dp[i][j][k]


ans = dp[D][K][0] + dp[D][K][1]
print(ans)
