H, W = map(int, input().split())

A = [None for i in range(H)]

for i in range(H):
    A[i] = list(map(int, input().split()))

B = [None for i in range(H)]

for i in range(H):
    B[i] = list(map(int, input().split()))

C = [[0 for j in range(W)] for i in range(H)]

s = 0
for y in range(H):
    for x in range(W):
        C[y][x] = B[y][x] - A[y][x]

cnt = 0
for y in range(H-1):
    for x in range(W-1):
        cnt += abs(C[y][x])
        C[y+1][x] += -C[y][x]
        C[y][x+1] += -C[y][x]
        C[y+1][x+1] += -C[y][x]
        C[y][x] = 0

isOkay = True
for x in range(W):
    isOkay = isOkay and (C[H-1][x] == 0)

for y in range(H):
    isOkay = isOkay and (C[y][W-1] == 0)

if isOkay:
    print("Yes")
    print(cnt)
else:
    print("No")