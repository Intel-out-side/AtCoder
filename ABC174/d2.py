N = int(input())
c = list(input())

Nw, Nr = 0, 0
for i in range(len(c)):
    Nw += 1 if c[i] == "W" else 0
    Nr += 1 if c[i] == "R" else 0

if Nw == 0 or Nr == 0:
    print(0)
    exit()

left_w = 0
right_r = 0
if c[0] == "W":
    left_w = 1
    right_r = Nr
else:
    left_w = 0
    right_r = Nr - 1

#仕切りの位置をiの横とすると
ans = max(left_w, right_r)

for i in range(len(c)):
    if i > 0:
        if c[i] == "W":
            left_w += 1
        else:
            right_r -= 1
    swap = max(left_w, right_r)
    ans = min(swap, ans)
print(ans)
