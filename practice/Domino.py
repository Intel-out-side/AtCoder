N = 2
M = 3

grid = [["..."], [".x."], ["..."]]

#愚直実装
used = [[False for _ in range(M)] for _ in range(N)]
color = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        color[i][j] = 0 if grid[i][j] == "." else 1
#color == 1 -> x
#color == 0 -> .

res = 0

def rec(i:int, j:int, used:list):
    global res

    used = used.copy()
    #端まで来た
    if j == M:
        return rec(i+1, j, used)

    #すべて敷き詰め終わった場合
    if i == N:
        return 1

    if used[i][j] or color[i][j]:
        # (j, i)にはブロックを置く必要がない
        return rec(i, j+1, used)

    res = 0
    used[i][j] = True

    #横向き
    if (j+1 < M) and (not used[i+1][j]) and (not color[i+1][j]):
        used[i][j+1] = True
        res += rec(i, j+1, used)
        used[i][j+1] = False

    #縦向き
    if (i+1 < N) and (not used[i+1][j]) and (not color[i+1][j]):
        used[i+1][j] = True
        res += rec(i+1, j, used)
        used[i+1][j] = False

    used[i][j] = False
    return res%M

ans = rec(0, 0, used)
