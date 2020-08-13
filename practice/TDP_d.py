W = int(input())
N, K = list(map(int, input().split()))

A, B = [0]*N, [0]*N

for i in range(N):
    a, b = list(map(int, input().split()))

    A[i], B[i] = a, b

dp = [[[0 for _ in range(W+1)] for _ in range(K+1)] for _ in range(N+1)]




import pprint
pprint.pprint(dp)
print(dp[K][W])
