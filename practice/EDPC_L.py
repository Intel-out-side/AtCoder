N = int(input())
a = list(map(int, input().split()))

dp = [[0 for _ in range(3100)] for _ in range(3100)]
# dp[i][j] := 区間[i,j)を抜き出した局面から出発して互いに最善テを打ったときのX-Yの値

for length in range(1, N+1):
    i = 0
    while i+length <= N:
        j = i + length

        if (N - length) % 2 == 0:
            dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j-1] + a[j-1])

        else:
            dp[i][j] = min(dp[i+1][j] - a[i], dp[i][j-1] - a[j-1])

        i += 1

ans = dp[0][N]
print(ans)
