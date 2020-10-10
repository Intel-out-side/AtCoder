N = int(input())
k = 2 * 10**5
MOD = 10**9 + 7

modinv = [-1] * (N+1)
modinv[1] = 1

for i in range(2, N+1):
    modinv[i] = (-modinv[MOD%i] * (MOD//i)) % MOD

def nCr(n, r):
    ans = 1
    for i in range(r):
        ans *= n - i
        ans *= modinv[i+1]
        ans %= MOD
    return ans

ans = 0
for i in range(2, N+1):

    ans += (2**i - 2) * nCr(N, i) * pow(8,N-i)
    ans %= MOD
print(ans)
