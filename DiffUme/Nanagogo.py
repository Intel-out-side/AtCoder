import itertools
from collections import Counter

N = int(input())
digits = len(str(N))
strNum = str(N)

li = ("7", "5", "3")

ans = 0

for i in range(1, digits+1):
    cand = list(itertools.product(li, repeat = i))
    # print(cand)

    for item in cand:
        c = Counter(item)
        if len(c.keys()) < 3:
            continue

        n = int("".join(item))
        # print(n)
        if n > N:
            continue

        ans += 1



print(ans)
