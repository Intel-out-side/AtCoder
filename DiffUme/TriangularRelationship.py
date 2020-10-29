N, K = map(int, input().split())

ans = None
if K % 2 == 0:
    evens = N // K
    odds = 0
    for i in range(1, N+1):
        if i % K == K//2:
            odds += 1
    ans = evens**3 + odds**3

if K % 2 == 1:
    t = N // K

    ans = t**3

print(ans)
