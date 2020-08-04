N, D = list(map(int, input().split()))

cod = [0]*N

for i in range(N):
    x, y = list(map(int, input().split()))
    cod[i] = (x, y)

ans = 0
for i in range(N):
    x, y = cod[i]

    if (x**2 + y**2) <= D**2:
        ans += 1

print(ans)
