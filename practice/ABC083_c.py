import math
X, Y = list(map(int, input().split()))

val = X
cnt = 1

while val <= Y:

    val *= 2
    cnt += 1

print(cnt - 1)
