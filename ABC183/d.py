N, W = map(int, input().split())

water = []
for i in range(N):
    t = tuple(map(int, input().split()))
    water.append(t)

asum = [0] * (2*10**5+1)

#始点でソート
water.sort(key=lambda x:x[0])

for w in water:
    asum[w[0]] += w[2]

#終点でソート
water.sort(key=lambda x:x[1])

for w in water:
    asum[w[1]] -= w[2]

for i in range(2*10**5):
    asum[i+1] += asum[i]

for x in asum:
    if x > W:
        print("No")
        exit()

print("Yes")
