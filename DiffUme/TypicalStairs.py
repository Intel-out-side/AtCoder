from collections import defaultdict
N, M = map(int, input().split())

memo = defaultdict(int)

def dfs(now):

    if now == N-2:
        return 2

    if now == N-1:
        return 1

    if now == N:
        return 1

    if not memo[now+1]:
        memo[now+1] = dfs(now+1)

    if not memo[now+2]:
        memo[now+2] = dfs(now+2)

    return memo[now+1] + memo[now+2]

memo[0] = dfs(0)

fibo = [0] * (N+1)
fibo[0] = 1
fibo[1] = 1
for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

tmp = 0
ans = memo[0]
for i in range(M):
    a = int(input())
    ans -= memo[a] * (fibo[a] - tmp)
    tmp += fibo[a]

print(ans % (10**9+7))
