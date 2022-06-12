N, M = map(int, input().split())

B = [None for _ in range(N)]

for i in range(N):
    B[i] = list(map(int, input().split()))

isOkay = True

for y in range(1, N):
    if B[y-1][0] + 7 != B[y][0]:
        isOkay = False

for y in range(N):
    for x in range(1, M):
        if B[y][x-1] + 1 != B[y][x]:
            isOkay = False

# 7で割り切れるやつが右端以外にある
for x in range(M-1):
    if B[0][x] % 7 == 0:
        isOkay=False
        

if isOkay:
    print("Yes")
else:
    print("No")