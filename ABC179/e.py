N, X, M = map(int, input().split())

ans = 0
start = X % M
An = X % M
rList = []
repeat = 1
repeatStart = None
while True:
    ans += An
    rList.append(An)
    An = An**2 % M
    repeat += 1
    if An in rList:
        repeatStart = An
        break
# print(rList, repeatStart)

repStartIndex = rList.index(repeatStart)

extraPart = rList[0:repStartIndex]
repPart = rList[repStartIndex:]
# print(extraPart, repPart)
extraLen = len(extraPart)
repLen = len(repPart)

ans += (((N - extraLen) // repLen) - 1)* sum(repPart)


if (N - extraLen) % repLen > 0:
    rest = (N-extraLen) % repLen
    for i in range(rest):
        ans += repPart[i]
print(ans)
