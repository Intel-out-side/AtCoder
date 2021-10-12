H, W = list(map(int, input().split()))

A = [0 for _ in range(H)]

for y in range(H):
    A[y] = list(map(int, input().split()))

colSum = [0] * W
rowSum = [0] * H

for y in range(H):
    tmp = 0
    for x in range(W):
        tmp += A[y][x]
    rowSum[y] = tmp

for x in range(W):
    tmp = 0
    for y in range(H):
        tmp += A[y][x]

    colSum[x] = tmp

ans = [[0 for _ in range(W)] for _ in range(H)]

for y in range(H):
    for x in range(W):
        ans[y][x] = rowSum[y] + colSum[x] - A[y][x]

for y in range(H):
    print(*ans[y])