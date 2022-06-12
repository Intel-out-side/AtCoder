H, W = map(int, input().split())

G = [[] for _ in range(H)]

for i in range(H):
    G[i] = list(map(int, input().split()))

isOkay = True
for i1 in range(H-1):
    for i2 in range(i1+1, H):
        for j1 in range(W-1):
            for j2 in range(j1+1, W):
                # Sval = G[i1][j1] + G[j2][j2] > G[i2][j1] + G[i1][j2]
                if G[i1][j1] + G[i2][j2] > G[i2][j1] + G[i1][j2]:
                    isOkay = False

if isOkay:
    print("Yes") 
else:
    print("No")