N = int(input())
A, B, C = map(int, input().split())

ans = 10**9
for x in range(0, 10000):
    for y in range(0, 10000-x):

        if (N - A*x - B*y) < 0:
            continue
        if (N - (A*x + B*y))%C == 0:
            z = (N - A*x - B*y) // C
            if x+y+z > 9999:
                continue
            ans = min(ans, x+y+z)
        else:
            continue

print(ans)