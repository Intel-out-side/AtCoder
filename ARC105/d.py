N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353

fact = [0] * (K+1)
fact[0] = 1
for i in range(1, K+1):
    fact[i] = i * fact[i-1] % MOD

val = [0] * (K+1)

for k in range(K+1):
    for n in range(1, N+1):

        val[k] += A[n-1]**k//fact[k]

mins = [0] * (K+1)

for i in range(1, K+1):
    tmp = 0
    for i in range(N):
        tmp += (A[i]+A[i])**i
    mins[i] = tmp

for k in range(1, K+1):
    ans = 0

    for i in range(0, k+1):
        ans += val[i] * val[k - i]
        ans %= MOD

    ans *= fact[k]

    ans -= mins[k]
    ans //= 2

    ans = (ans + MOD) % MOD
    print(ans)
