import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(n-r)*math.factorial(r))

N, M, A, B = map(int, input().split())
MOD = 998244353

zentai = nCr(N+M, N) % MOD
if (N<A) or (M<B):
    ans = zentai
    print(ans)
    exit()

route1 = nCr(A+B, A) % MOD

route2 = nCr(N+M-A-B, N-A) % MOD


ans = zentai - route1*route2
ans %= MOD

print(ans)