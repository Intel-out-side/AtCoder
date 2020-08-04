import itertools
from collections import deque

N, M = list(map(int, input().split()))

g = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0

for root in itertools.permutations(range(1, N), N-1):
    root = [0] + list(root)
    print(root)
    print(root, root[1:])
    if all(a in g[b] for a, b in zip(root, root[1:])):
        #並び替えたときに次の点に行ける様に辺が接続されているかどうか
        ans += 1
print(ans)
