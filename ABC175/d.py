import sys
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    P[i] -= 1
C = list(map(int, input().split()))

memo = [[None for _ in range(K+1)] for _ in range(N)]

def f(now, count, nowVal, maxVal):
    if count == K:
        # print(max(maxVal, nowVal + C[P[now]]))
        return max(maxVal, nowVal + C[P[now]])

    tmpMax = max(maxVal, nowVal + C[P[now]])
    return f(P[now], count+1, nowVal+C[P[now]], tmpMax)

ans = -float("inf")
for i in range(N):
    ans = max(ans, f(i, 0, 0, -float("inf")))

print(ans)
