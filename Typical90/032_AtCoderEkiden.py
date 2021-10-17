# pythonはitertoolsで順列組み合わせを生成できる

from itertools import permutations

N = int(input())

runners = [i for i in range(N)]
A = [None for _ in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    
    A[i] = tmp

isAdjOkay = [[True for _ in range(N)] for _ in range(N)]

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())

    isAdjOkay[x-1][y-1] = False
    isAdjOkay[y-1][x-1] = False

ans = 10**9
for pattern in permutations(runners):

    isValidPerm = True
    for i in range(1, N):
        if not isAdjOkay[pattern[i-1]][pattern[i]]:
            isValidPerm = False

    if not isValidPerm:
        continue
    
    tmp = 0
    for i in range(N):
        tmp += A[pattern[i]][i]

    ans = min(ans, tmp)


if ans == 10**9:
    print(-1)
else:
    print(ans)