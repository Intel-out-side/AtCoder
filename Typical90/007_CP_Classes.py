N = int(input())
A = list(map(int, input().split()))
A.sort() #単調増加にする．
Q = int(input())

for i in range(Q):
    left = 0
    right = N-1
    mid = None
    isFound = False
    B = int(input())

    while left+1 < right:
        mid = (left + right) // 2

        if A[mid] - B == 0:
            isFound = True
            break
        elif A[mid] - B < 0:
            left = mid
        else:
            right = mid
    if isFound:
        ans = 0
    else:
        ans = min(abs(A[left] - B), abs(A[right] - B))

    print(ans)