import math
X, K, D = list(map(int, input().split()))

a = (K * D - X) / (2*D)
a1, a2 = math.floor(a), math.ceil(a)

left = 0
right = K
def f(a):
    return X - K * D + 2 * a * D

mid = None
flag = 0
while left+1 < right:
    mid = (left + right) // 2

    if f(mid) == 0:
        flag = 1
        break
    elif f(mid) < 0:
        left = mid
    else:
        right = mid

if flag:
    print(abs(X - K * D + 2 * mid * D))
else:
    res1 = abs(X - K * D + 2 * left * D)
    res2 = abs(X - K * D + 2 * right * D)
    print(min(res1, res2))
