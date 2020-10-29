import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

def identify(x):
    tmp = 0
    for item in A:
        tmp += math.ceil(item/x)-1

    if tmp <= K:
        return 1
    else:
        return 0

left = 0
right = max(A) + 1

mid = None
found = False

while left+1<right:
    mid = (left + right) // 2

    if identify(mid) == 0:
        left = mid
    else:
        right = mid

print(right)
