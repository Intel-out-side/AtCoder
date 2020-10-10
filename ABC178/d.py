S = int(input())
if S < 3:
    print(0)
    exit()

MOD = 10**9 + 7
fact = [1] * (S+1)
for i in range(2, S+1):
    fact[i] = i * fact[i-1]

def nCr(n, r):
    return fact[n] // (fact[r] * fact[n-r])

boxes = S//3
ans = 0
for box in range(2, boxes+1):
    balls = S - box*3
    ans += nCr(balls + box - 1, balls) % MOD
    ans %= MOD

ans += 1
ans = ans % MOD

print(ans)
