import math
X, Y, A, B = map(int, input().split())

ans = 0
for a in range(100):

    if Y - X*(A**a) <= 0:
        continue

    b = (Y - X*(A**a))//B

    if (Y - X*(A**a)) % B == 0:
        b -= 1

    ans = max(ans, a+b)

print(ans)
