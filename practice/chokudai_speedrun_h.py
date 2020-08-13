
N = int(input())
A = list(map(int, input().split()))
"""
# O(N^2)なのでTLE
dp = [1 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))
"""

def lower_bound(li, val):
    left = 0
    right = len(li)-1
    mid = None
    while left < right:
        mid = (left + right)//2

        if li[mid] < val:
            left = mid + 1
        else:
            right = mid

    return left

dp = [float("inf") for _ in range(N)]

for i in range(N):
    pos = lower_bound(dp, A[i])
    dp[pos] = A[i]

ans = 0
for i in range(N):
    if dp[i] < (10**6 + 1):
        ans += 1
print(ans)
