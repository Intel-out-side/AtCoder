N, M = list(map(int, input().split()))

relations = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = list(map(int, input().split()))

    relations[x-1][y-1] = 1
    relations[y-1][x-1] = 1

ans = 0
for i in range(2**N): # N人に関してのbit全探索を考える
    tmp = 0
    habatsu = []
    for j in range(N):
        isIncluded = (i >> j) & 1

        if isIncluded:
            habatsu.append(j)

    isValidHabatsu = True
    for k in range(len(habatsu)):
        for o in range(len(habatsu)):
            if k == o:
                continue
            if relations[habatsu[k]][habatsu[o]] == 0:
                isValidHabatsu = False

    if isValidHabatsu:
        ans = max(ans, len(habatsu))

print(ans)
