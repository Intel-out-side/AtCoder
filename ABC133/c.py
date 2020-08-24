L, R = map(int, input().split())

ans = 2020
if R - L < 2019:
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            ans = min((i*j)%2019, ans)

else:
    for i in range(L, L+2019):
        for j in range(i+1, L+2019):
            ans = min((i*j)%2019, ans)

print(ans)
