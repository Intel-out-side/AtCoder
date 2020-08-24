N = int(input())
v = list(map(int, input().split()))

v.sort()

num = v[0]+v[1]
den = 2
for i in range(2, N):
    num += den * v[i]
    den *= 2

ans = num / den
print(ans)
