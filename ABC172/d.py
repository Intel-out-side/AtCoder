import math
import sys

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

N = int(input())

ans = 0

for k in range(1, N+1):

    if k == 1:
        ans += 1
    else:
        ans += k * len(make_divisors(k))

print(ans)
