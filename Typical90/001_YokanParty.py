# 最小値の最大値を求める問題→答えで二分探索で解ける場合がある

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) + [L]

for i in range(N, 0, -1):
    A[i] -= A[i-1]

def isDivisibleBy(x):
    tmp = 0
    divideCount = 0
    total = 0

    for i in range(N+1):
        tmp += A[i]
        total += A[i]
        
        if tmp >= x and L-total>=x:
            divideCount += 1
            tmp = 0

    
    if divideCount < K:
        return False

    return True

left  = 0
right = L+1
while left+1 < right:

    mid = (left + right)//2

    if isDivisibleBy(mid):
        left = mid
    else:
        right = mid

ans = left
print(ans)