import time
N = int(input())
A = list(map(int, input().split()))

left = 0
right = left + 1
money = 1000

while left < N - 1:

    if A[left] >= A[left+1]:
        left += 1
        right = left
        continue

    if right <= N-2:
        if A[right] <= A[right+1]:
            right += 1
            continue

    money += (money//A[left]) * (A[right]-A[left])
    left = right

print(money)
