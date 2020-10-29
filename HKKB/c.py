N = int(input())
p = list(map(int, input().split()))

tmp = -1
isUsed = [False] * 200001
isUsed[p[0]] = True
if p[0] == 0:
    tmp = 1
else:
    tmp = 0

print(tmp)

for i in range(1, N):
    if tmp == p[i]:
        pos = tmp
        isUsed[tmp] = True
        while isUsed[pos]:
            pos += 1
        tmp = pos
        print(tmp)
    else:
        isUsed[p[i]] = True
        print(tmp)
