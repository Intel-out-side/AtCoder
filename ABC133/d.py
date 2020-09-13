N = int(input())
A = list(map(int, input().split()))

S = sum(A)

M = [0 for _ in range(N)]

M0 = S

for i in range(1, N, 2):
    M0 -= 2*A[i]

M[0] = M0

for i in range(1, N):
    M[i] = 2*A[i-1] - M[i-1]


print(*M)
