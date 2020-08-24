import pprint
H, W, M = map(int, input().split())
bombs = [[0 for _ in range(W)] for _ in range(H)]
hCount = [0]*H
vCount = [0]*W

for i in range(M):
    h, w = map(int, input().split())
    h -= 1; w -= 1;
    hCount[h] += 1
    vCount[w] += 1
    bombs[h][w] = 1

hMax = max(hCount)
vMax = max(vCount)
hMaxIndex = [i for i, x in enumerate(hCount) if x==max(hCount)]
vMaxIndex = [i for i, x in enumerate(vCount) if x==max(vCount)]

ans = -1
for y in hMaxIndex:
    for x in vMaxIndex:
        if bombs[y][x]:
            ans = max(hMax + vMax - 1, ans)
        else:
            ans = max(hMax+vMax, ans)
print(ans)
