from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

maxVal = N + max(A)
ans = 0

candidatesL = defaultdict(int)
for i in range(1, N+1):
    candidatesL[i+A[i-1]] += 1

candidatesR = defaultdict(int)
for j in range(1, N+1):
    candidatesR[j-A[j-1]] += 1

ans = 0
for x in candidatesL.keys():
    ans += candidatesL[x] * candidatesR[x]

print(ans)
