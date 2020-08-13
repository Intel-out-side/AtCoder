N, W = map(int, input().split())

value, weight = [0]*N, [0]*N

for i in range(N):
    v, w = map(int, input().split())
    value[i], weight[i] = v, w

dp = [[]]
