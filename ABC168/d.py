from collections import deque
N, M = list(map(int, input().split()))

g = [[] for _ in range(N)]
sign = [-1 for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))

    g[a-1].append(b-1)
    g[b-1].append(a-1)

queue = deque()
queue.append(0)

while len(queue) > 0:

    now = queue.popleft()

    for adj in g[now]:
        if sign[adj] == -1:
            queue.append(adj)
            sign[adj] = now


allVisited = True

for i in range(1, len(sign)):
    if sign[i] == -1:
        allVisited = False

if not allVisited:
    print("No")
    exit()

else:
    print("Yes")
    for i in range(1, len(sign)):
        print(sign[i]+1)
