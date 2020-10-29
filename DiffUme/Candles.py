import heapq
N, K = map(int, input().split())
x = list(map(int, input().split()))

#連続するK個につけるのが最適
ans = float("inf")
for i in range(N-K+1):

    l = x[i]
    r = x[i+K-1]

    a = abs(l) + abs(r-l)
    b = abs(r) + abs(r-l)

    ans = min(ans, min(a, b))

print(ans)
