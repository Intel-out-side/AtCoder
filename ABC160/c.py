K, N = map(int, input().split())

A = list(map(int, input().split()))

if len(A) == 2:
    dist = A[1] - A[0]
    if 2 * dist > K:
        dist = K - dist

minDist = float("inf")
for i in range(N-1):
    if K - (A[i+1] - A[i]) < minDist:
        minDist = K - (A[i+1] - A[i])

minDist = min(minDist, A[N-1]-A[0])

print(minDist)
