N = int(input())

t = [0]*N

for i in range(N):
    t[i] = int(input())

ans = float("inf")

for i in range(2**N):
    tmpA = 0
    tmpB = 0
    for j in range(N):

        #肉焼き機Aの時間
        if (i >> j) & 1:
            tmpA += t[j]
        else:
            tmpB += t[j]

    ans = min(ans, max(tmpA, tmpB))

print(ans)
