N, K = map(int, input().split())
A = list(map(int, input().split()))

S = str(K)
D = len(str(K))

allXOR = 0

for item in A:
    allXOR = allXOR ^ item

dp = [[0 for _ in range(2)] for _ in range(D+1)]
#dp[i桁目まで決定した][0->N桁目まで一致 1->N以下であることが確定している]

for i in range(D):
    for j in range(2):

        for digit in range(10):

            if j == 0:

                if digit > int(S[i]):
                    continue

                if digit == int(S[i]):
                    dp[i+1][j] = max(dp[i][j], )
