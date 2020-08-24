N = int(input())

ans = 0
for i in range(1, N+1):
    num = str(i)
    if len(num) % 2 == 1:
        ans += 1

print(ans)
