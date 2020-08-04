from collections import deque
N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

score = [0]*N
dq = deque()

score_now = 1
for i in range(0, K):
    dq.append(A[i])
    score_now *= A[i]
    score_now %= 10**9 + 7

for j in range(K-1, N-1):
    score[j] = score_nowd

    left = dq.popleft()
    score_now /= left
    dq.append(A[j+1])
    score_now *= A[j+1]
score[N-1] = score_now % (10**9 + 7)

for k in range(K, N):
    if score[k] > score[k-1]:
        print("Yes")
    else:
        print("No")
