#区間スケジューリング問題

N = int(input())

robots = {}

for _ in range(N):
    X, L = list(map(int, input().split()))

    robots[X] = (X-L, X+L)

#終端が早い順にソートして、取れるものから貪欲法でとっていく

robots_sorted = sorted(robots.items(), key=lambda x:x[1][1])
print(robots_sorted)

ans = 1
current_robot = robots_sorted[0]

for i in range(0, N):
    if current_robot[1][1] > robots_sorted[i][1][0]:
        continue

    ans += 1
    current_robot = robots_sorted[i]


print(ans)
