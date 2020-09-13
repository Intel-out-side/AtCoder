N = int(input())
A = list(map(int, input().split()))

accSum = [0]*N
accSum[0] = A[0]
for i in range(1, N):
    accSum[i] = accSum[i-1] + A[i]
S = sum(A)

ans = 0

for i in range(N):
    ans += A[i] * (S - accSum[i]) % (10**9+7)
ans = ans % (10**9+7)
print(ans)
