N, K = map(int, input().split())


k = [1 for _ in range(N+1)]
for i in range(2, N+1):
    k[i] = (i) * k[i-1]
# print(k)

def C(n, r):
    return k[n] // (k[r] * k[n-r])

red = N-K
blue = K
for i in range(1, K+1):
    # print(red+1, blue-1, i)
    # print(C(red+1, i), C(blue-1, i-1))
    ans = C(red+1, i) * C(blue-1, i-1)

    print(ans % (10**9+7))
