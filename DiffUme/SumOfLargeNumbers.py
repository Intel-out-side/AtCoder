N, K = map(int, input().split())
S = N * (N+1) // 2

A = [0 for _ in range(N+1)]
for i in range(1, N+1):
    A[i] = i * (i+1) // 2

ans = 0
for j in range(K, N+2):
    minSum = j * (j-1) // 2
    maxSum = S - (N-j)*(N-j+1)//2
    possibleSums = maxSum - minSum + 1
    ans += possibleSums % (10**9 + 7)
ans %= (10**9 + 7)
print(ans)
