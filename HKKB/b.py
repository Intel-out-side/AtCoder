H, W = map(int, input().split())

grid = []

for i in range(H):
    grid.append(input())

ans = 0
for y in range(H):
    for x in range(W-1):
        if grid[y][x] == "." and grid[y][x+1] == ".":
            ans += 1

for x in range(W):
    for y in range(H-1):
        if grid[y][x] == "." and grid[y+1][x] == ".":
            ans += 1

print(ans)
