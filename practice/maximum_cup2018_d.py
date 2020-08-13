import math
N, M, L, X = map(int, input().split())

a = list(map(int, input().split()))

dp = [[0 for _ in range(M)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):

        if j == 0:
            dp[i+1][j] = 1
        else:
            res1 = dp[i][j]
            res2 = dp[i][(j + a[i])%M] + math.floor((j+a[i])/M)

            dp[i+1][j] = min(res1, res2)

import pprint
pprint.pprint(dp)
if dp[N][L] <= X:
    print("Yes")
else:
    print("No")
