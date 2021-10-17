import math
A, B = map(int, input().split())

ans = A*B // math.gcd(A, B)

if ans > 10**18:
    print("Large")
else:
    print(ans)

#1000000000000000000 1000000000000000000