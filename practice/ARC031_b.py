import sys
import pprint
sys.setrecursionlimit(10**7)

place = []
H, W = 10, 10

for i in range(H):
    place.append(list(input()))

visited = [[False for _ in range(W)] for _ in range(H)]

def dfs(i, j, num):
    if i < 0 or i >= H or j < 0 or j >= W:
        return

    if place[i][j] == "x" or visited[i][j]:
        return

    if place[i][j] == "o":
        visited[i][j] = True
        place[i][j] = num

    dfs(i+1, j, num)
    dfs(i, j+1, num)
    dfs(i-1, j, num)
    dfs(i, j-1, num)

islands = []
num = 0
for i in range(H):
    for j in range(W):
        if place[i][j] == 'o':
            dfs(i, j, num)
            islands.append(num)
            num += 1
#現在numが陸地の数に等しい
islands.sort()

if num == 1:
    print("YES")
    sys.exit()
    #陸地が元から一つのみの場合

for i in range(H):
    for j in range(W):
        ans = []
        if place[i][j] == "x":

            dx_ = [1, 0, -1, 0]
            dy_ = [0, 1, 0, -1]

            for (dx, dy) in zip(dx_, dy_):
                if not 0 <= i+dx < H or not 0 <= j+dy < W:
                    continue

                if isinstance(place[i+dx][j+dy], int):
                    if not place[i+dx][j+dy] in ans:
                        ans.append(place[i+dx][j+dy])
                        # 同じ島がコの字になってる場合がある
            ans.sort()

            if islands == ans:
                print("YES")
                sys.exit()

print("NO")
