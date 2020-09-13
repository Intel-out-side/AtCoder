N = int(input())
A = list(map(int, input().split()))

M = [0] * N
S = 0
for i in range(N):
    S = S^A[i]

for i in range(N):
    M[i] = S^A[i]

print(*M)
