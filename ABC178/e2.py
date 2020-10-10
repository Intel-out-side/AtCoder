N = int(input())

x, y = [0]*N, [0]*N

for i in range(N):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b

maxZ, minZ = x[0] + y[0], x[0] + y[0]
maxW, minW = x[0] - y[0], x[0] - y[0]
for i in range(N):
    z = x[i] + y[i]
    w = x[i] - y[i]

    maxZ = max(maxZ, z)
    minZ = min(minZ, z)
    maxW = max(maxW, w)
    minW = min(minW, w)

ans = max(maxZ-minZ, maxW-minW)
print(ans)
