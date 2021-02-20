from itertools import permutations
N, K = map(int, input().split())

T = []

for i in range(N):
    l = list(map(int, input().split()))
    T.append(l)

city = [i for i in range(1, N)]

ans = 0
for o in list(permutations(city)):
    time = 0
    order = (0,) + o + (0, )

    for i in range(N):
        s = order[i]
        g = order[i+1]

        time += T[s][g]

    if time == K:
        ans += 1

print(ans)
