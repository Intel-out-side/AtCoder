import math
N, K = map(int, input().split())

ans = 0
for i in range(1, K):
    if i > N:
        break
    x = math.ceil(math.log2(K/i))
    p = (1/2)**x
    ans += p

ans *= 1/N

if N >= K:
    ans += (N-K+1)/N

print("{:.10f}".format(ans))
