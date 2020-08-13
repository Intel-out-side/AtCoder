import pprint
N, W = list(map(int, input().split()))

value = [0]*N
weight = [0]*N

for i in range(N):
    v, w = list(map(int, input().split()))
    value[i] = v
    weight[i] = w

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

#ゼロ個選ぶ場合は価値の総和の最大値は常にゼロ
for w in range(W):
    dp[0][w] = 0

for i in range(N):
    for w in range(W+1):

        if weight[i] <= w:
            dp[i+1][w] = dp[i][w - weight[i]] + value[i]
        else:
            dp[i+1][w] = dp[i][w]

pprint.pprint(dp)
print(dp[N][W])
