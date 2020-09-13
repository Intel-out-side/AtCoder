import pprint
H, W, M = map(int, input().split())
bombs = set()
hCount = [0]*H
vCount = [0]*W

for i in range(M):
    h, w = map(int, input().split())
    h -= 1; w -= 1;
    hCount[h] += 1
    vCount[w] += 1
    bombs.add((h, w))

hMax = max(hCount)
vMax = max(vCount)
hMaxIndex = [i for i, x in enumerate(hCount) if x==hMax]
vMaxIndex = [i for i, x in enumerate(vCount) if x==vMax]

ans = -1
for x in vMaxIndex:
    for y in hMaxIndex:
        #continueするのはたかだかM回
        
        if (y, x) in bombs:
            continue
        else:
            print(hMax + vMax)
            exit()
print(hMax + vMax - 1)
