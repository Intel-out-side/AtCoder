H, W = Hap(int, input().split())

grid = [0 for _ in range(H)]

for i in range(H):
    grid[i] = input()

#愚直実装
ans = 0
def search(x, y):
    global ans

    if x == W and y == H:
        ans = ans + 1
        return

    else:
        if grid[y][x] == "?":

            grid[y][x] = "J"
            if grid[y][x+1] != "O" and grid[y+1][x] != "I":
                search(y, x+1)

            grid[y][x] = "O"
            if grid[y][x-1] != "O" and grid[y+1][x-1] != "I":
                search(y, x+1)

            grid[y][x] = "I"
            if grid[y-1][x] != "J" and grid[y-1][x+1] != "I":
                search(y, x+1)

        else:
            #grid[y][x]に元の文字を当てはめる
            if grid[y][x] == "J":
                #もし良いJOIが生じなかった

            elif grid[y][x] == "O":
                #もし良いJOIが生じなかった

            else:
                #もし良いJOIが生じなかった

def search(x, y, sx, sy):

    if x == sx:
        return


for y in range(H):
    for x in range(W):

        now = (x, y)
