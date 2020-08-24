N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [P[i]-1 for i in range(N)]
ans = -float("inf")

for start in range(N):
    x = start
    pattern = []
    while True:
        x = P[x]
        pattern.append(x)
        if x == start:
            break

    pattern_len = len(pattern)
    total = 0
    if pattern_len >= K:
        for j in range(K):
            total += C[pattern[j]]
            ans = max(ans, total)
    else:
        for j in range(pattern_len):
            total += C[pattern[j]]
        if total <= 0:
            now = 0
            for j in range(pattern_len):
                now += C[pattern[j]]
                ans = max(now, ans)
        else:
            now = 0
            now += total * (K // pattern_len)
            for j in range(K % pattern_len):
                now += C[pattern[j]]
                ans = max(ans, now)
print(ans)
