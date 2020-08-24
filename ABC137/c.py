from collections import Counter
from collections import defaultdict
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N = int(input())

s = [0] * N

patterns = defaultdict(int)

for i in range(N):
    s[i] = input()

    list_string = list(s[i])
    list_string.sort()

    list_string = "".join(list_string)
    patterns[list_string] += 1

ans = 0
for p in patterns.values():
    if p >= 2:
        ans += comb(p, 2)

print(ans)
