N, K = map(int, input().split())

MOD = 10**9 + 7

def repetitive_pow(x, n, mod=1):

    ans = 1
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n = n>>1
    return ans

if N >= 3 and K <= 2:
    ans = 0
elif N == 2 and K == 2:
    ans = 2
elif N == 2 and K == 1:
    ans = 0
elif N == 1:
    ans = K
else:
    ans = K * (K-1) * repetitive_pow(K-2, N-2)
    ans %= MOD

print(ans)