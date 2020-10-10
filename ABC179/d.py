N, K = map(int, input().split())
MOD = 998244353
span = []
for i in range(K):
    l, r = map(int, input().split())
    span = span + list(range(l, r+1))

start = 0 #0-indexed
def dfs(now):
    f


ans = len(span) ** N % MOD
print(ans)
