N = int(input())
p = list(map(float, input().split()))

if N == 1:
    print(p)

dp = [0] * (N+1)

minHead = N // 2 + 1 #表になる最小枚数

for i in range(minHead, N+1):
