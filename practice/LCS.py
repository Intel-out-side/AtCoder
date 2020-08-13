N = int(input())

ans = []

for _ in range(N):
    X = input()
    Y = input()

    dp = [[0 for _ in range(len(X)+1)] for _ in range(len(Y)+1)]

    for i in range(len(Y)):
        for j in range(len(X)):
            if X[j] == Y[i]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    ans.append(dp[len(Y)][len(X)])

for a in ans:
    print(a)
