import math
N, K = map(int, input().split())

L = []

for _ in range(N):
    a, b = map(int, input().split())

    L.append(b)
    L.append(a-b)

L.sort(reverse=True)

print(sum(L[0:K]))