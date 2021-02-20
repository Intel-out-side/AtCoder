N = input()
D = len(N)

S = 0
for d in N:
    S += int(d)

if S < 3:
    print(-1)
    exit()

if S % 3 == 0:
    print(0)
    exit()

ans = float("inf")

for i in range(1, 1<<D):
    if i == (1<<D)-1:
        continue
    cnt = 0
    tmp = S
    for j in range(D):
        if (i >> j) & 1:
            tmp -= int(N[j])
            cnt += 1

    if tmp % 3 == 0:
        ans = min(ans, cnt)

if ans == float("inf"):
    ans = -1

print(ans)
