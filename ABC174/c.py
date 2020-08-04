import sys
import math
K = int(input())

#２の倍数のとき
if K % 2 == 0:
    print(-1)
    sys.exit()

if K % 7 == 0:
    K /= 7

val = 1
count = 0
pow = 10

while True:

    if val % K == 0:
        print(count)
        sys.exit()

    val += pow
    pow *= 10
    count += 1
