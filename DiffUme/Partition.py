N, M = map(int, input().split())

from collections import defaultdict
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

factors = factorize(M)

possibleDividers = []

for key, val in factors.items():

    for i in range(1, val+1):
        possibleDividers.append(key**i)

possibleDividers.sort()

minDiv = float("inf")
for item in possibleDividers:
    if item >= N:
        minDiv = min(item, minDiv)

print(possibleDividers)
if minDiv == float("inf"):
    print(1)
    exit()

ans = M // minDiv

print(ans)
