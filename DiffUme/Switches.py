from collections import defaultdict
N, M = map(int, input().split())

connection = {}
for i in range(M):
    line = list(map(int, input().split()))
    s = line[1:]
    connection[i] = s

P = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    isSwitchOn = [0 for _ in range(N)]
    for j in range(N):
        if (i >> j) & 1:
            isSwitchOn[j] = 1

    onBulbs = 0
    for j in range(M):
        count = 0
        for switch in connection[j]:
            if isSwitchOn[switch-1]:
                count += 1

        if count % 2 == P[j]:
            onBulbs += 1

    if onBulbs == M:
        ans += 1

print(ans)
