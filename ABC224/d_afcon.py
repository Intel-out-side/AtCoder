from itertools import permutations
from collections import defaultdict, deque
N = int(input())

graph = defaultdict(list)

for i in range(N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

komaIsAt = list(map(lambda x:int(x)-1, input().split()))
nodeHasKomaOf = [str(komaIsAt.index(i)) if i in komaIsAt else "x" for i in range(9)]
GOAL = "01234567x"
initState = "".join(map(str, nodeHasKomaOf))
queue = deque()

queue.append(initState)
dist = dict()
dist[initState] = 0

def swap(tgt, i, j):
    tgt = list(tgt)

    tgt[i], tgt[j] = tgt[j], tgt[i]

    return "".join(tgt)

while queue:
    now = queue.popleft()
    
    for i in range(9):
        if now[i] == "x":
            emptyNode = i

    for adj in graph[emptyNode]:
        nextState = now #to be swapped
        nextState = swap(nextState, emptyNode, adj)
        if nextState in dist.keys():
            continue
        dist[nextState] = dist[now] + 1
        queue.append(nextState)

if not GOAL in dist.keys():
    print("-1")
else:
    print(dist[GOAL])