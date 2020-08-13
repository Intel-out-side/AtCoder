H, N = list(map(int, input().split()))

A, B = [0]*N, [0]*N

for i in range(N):
    a, b = list(map(int, input().split()))
    A[i], B[i] = a, b

maxCost = sum(B)

dp = [[0 for _ in range(maxCost+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(maxCost+1):

        if A[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            res1 = dp[i][j]
            res2 = dp[i+1][j - B[i]] + A[i]
            dp[i+1][j] = max(res1, res2)

# import pprint
# pprint.pprint(dp)
for i in range(maxCost+1):

    if dp[N][i] >= H:
        print(i)
        exit()
