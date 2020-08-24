S = input()
N = len(S)

# indexごとに次のLまでの距離を入れる
nextL = [0]*N
nextR = [0]*N

dist = 0
for i in range(N-1, -1, -1):
    if S[i] == 'R':
        dist += 1
        nextL[i] = dist
    else:
        dist = 0

dist = 0

for i in range(N):
    if S[i] == 'L':
        dist += 1
        nextR[i] = dist
    else:
        dist = 0

ans = [0]*N

for i in range(N):
    if S[i] == 'R':
        if nextL[i] % 2 == 0:
            ans[i + nextL[i]] += 1
        else:
            ans[i+nextL[i]-1] += 1

for i in range(N-1, -1, -1):
    if S[i] == 'L':
        if nextR[i] % 2 == 0:
            ans[i - nextR[i]] += 1
        else:
            ans[i - nextR[i] + 1] += 1

print(*ans)
