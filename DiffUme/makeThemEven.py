H, W = map(int, input().split())

grid = []

for i in range(H):
    grid.append(list(map(int, input().split())))

odds = []

for y in range(H):
    for x in range(W):
        if grid[y][x] % 2 == 1:
            odds.append((x, y))


numOfOdds = len(odds)
N = 0

moves = []

for i in range(0, numOfOdds, 2):

    sx, sy = odds[i]
    gx, gy = odds[i+1]

    N += abs(sx - sy) + abs(gx - gy)

    if sx < gx:
        for x in range(1, abs(sx - gx)+1):
            moves.append((sx, sy, sx+x, sy))

            sx += abs(sx-gx)
            if sy < gy:
                for y in range(1, abs(sy-gy)+1):
                    moves.append((sx, sy, sx, sy+y))
            else:
                for y in range(1, abs(sy-gy)+1):
                    moves.apppend((sx, sy, sx, sy-y))

    else:
        for x in range(1, abs(sx, gx)+1):
            moves.append((sx, sy, sx-x, sy))

            sx -= abs(sx-gx)
            if sy < gy:
                for y in range(1, abs(sy-gy)+1):
                    moves.append((sx, sy, sx, sy+y))
            else:
                for y in range(1, abs(sy-gy)+1):
                    moves.append((sx, sy, sx, sy-y))

print(N)
for item in moves:
    print(*item)
