N, M, X = map(int, input().split())

books = [0]*N
for i in range(N):
    books[i] = list(map(int, input().split()))

cost = float("inf")
for i in range(1<<N):
    scores = [0] * M
    tmpCost = 0

    for j in range(N):
        if (i >> j) & 1:
            tmpCost += books[j][0]
            scores = [scores[k] + books[j][k+1] for k in range(M)]

    isPossible = True
    for j in range(M):
        isPossible &= (X<=scores[j])

    if isPossible:
        cost = min(cost, tmpCost)

if cost < float("inf"):
    print(cost)
else:
    print(-1)
