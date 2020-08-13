import pprint
H, N = list(map(int, input().split()))

A, B = [0]*N, [0]*N


for i in range(N):
    a, b = list(map(int, input().split()))
    A[i], B[i] = a, b

maxDamage = H + max(A)

dp = [[float("inf") for _ in range(maxDamage+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(maxDamage+1):

        if j < A[i]:
            dp[i+1][j] = dp[i][j]

        else:
            res1 = dp[i][j]
            res2 = dp[i+1][j - A[i]] + B[i]

            dp[i+1][j] = min(res1, res2)

# pprint.pprint(dp)
print(min(dp[N][H:]))
