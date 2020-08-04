#区間スケジューリングで解けるらしい
N, M = list(map(int, input().split()))

bridges = [0 for i in range(N)]
l = [0]*M

for i in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    l[i] = (a, b)

l = sorted(l, key=lambda x:x[1])

current_bridge = l[0]
ans = 1

for relations in l:

    if current_bridge[1] > relations[0]:
        continue

    ans += 1
    current_bridge = relations

print(ans)
