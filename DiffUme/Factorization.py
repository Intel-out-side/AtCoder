from collections import defaultdict
import math
def factorize(n):
    i = 2
    factors = defaultdict(int)
    while i**2 <= n:
        if n % i != 0:
            i += 1
            continue

        while n % i == 0:
            n //= i
            factors[i] += 1
        i += 1

    if n != 1:
        factors[n] += 1

    return factors

def C(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

N, M = map(int, input().split())
factors = factorize(M)
# print(factors)

ans = 1
for key, val in factors.items():
    ans *= C(N + val - 1, val)

MOD = 10**9 + 7
print(ans % MOD)
