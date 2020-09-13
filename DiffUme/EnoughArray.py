N, K = map(int, input().split())
A = list(map(int, input().split()))
accSum = [A[0]]
for i in range(N-1):
    accSum.append(accSum[i] + A[i+1])
# print(accSum)

def getSum(start, i):
    if start == 0:
        return accSum[i]

    return accSum[i] - accSum[start - 1]

ans = 0
for i in range(N):
    if getSum(i, N-1) < K:
        continue
    if getSum(i, i) >= K:
        ans += N-1 - i + 1
        continue

    left = i
    right = N-1
    mid = None
    while left + 1 < right:
        mid = (left + right) // 2

        if getSum(i, mid) == K:
            right = mid
            break
        elif getSum(i, mid) < K:
            left = mid
        else:
            right = mid

    #left < val <= right
    ans += (N-1 - right) + 1
print(ans)
