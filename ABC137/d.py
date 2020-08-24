N, M = map(int, input().split())

A, B = [0]*N, [0]*N
for i in range(N):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

dp = [[0 for i in range(M+1)] for j in range(N+1)]
flag = [0 for _ in range(M+1)]

for i in range(N):
    for j in range(1, M + 1):
        if j < A[i]:
            dp[i+1][j] = dp[i][j]
        else:
            if flag[j-A[i]]:
                res1 = dp[i][j]
                res2 = dp[i][j - A[i]] + B[i]
                dp[i+1][j] = max(res1, res2)
            else:
                flag[j - A[i]] = 1
                dp[i+1][j] = dp[i][j] + B[i]

print(dp)
print(max(dp[N]))
