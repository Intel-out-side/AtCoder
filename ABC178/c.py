import math
N = int(input())

if N == 1:
    print(0)
    exit()
fac = [1] * (N+1)

for i in range(2, N+1):
    fac[i] = i * fac[i-1]

def C(n, r):
    return fac[n] // (fac[r] * fac[n - r])
ans = 0
for i in range(2, N+1):
    ans += (2**i - 2) * C(N, i) * 8 ** (N-i)
    ans %= 10**9 + 7
print(ans % (10**9 + 7))
