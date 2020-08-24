N = int(input())
H = list(map(int, input().split()))

maxLen = 0
tmp = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        tmp += 1
        maxLen = max(maxLen, tmp)
    else:
        tmp = 0

print(maxLen)
