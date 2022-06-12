from collections import defaultdict
N = int(input())

graph = defaultdict(list)
indeg = defaultdict(int)

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

    indeg[a] += 1
    indeg[b] += 1

isStar = False

for i in range(N):
    if indeg[i] == N-1:
        isStar = True

if isStar:
    print("Yes")
else:
    print("No")