N = input()

ans = 0
for i in range(len(N)):
    ans += int(N[i])

if ans % 9 == 0:
    print("Yes")
else:
    print("No")
