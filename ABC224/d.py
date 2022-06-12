from collections import defaultdict, deque
M = int(input())

graph = [[False for _ in range(9)] for _ in range(9)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = True
    graph[v][u] = True

p = list(map(int, input().split()))

koma_is_at = defaultdict(int)

for i in range(8):
    koma_is_at[i] = p[i] - 1

komasAtWrongNode = deque()
for key, value in koma_is_at.items():
    if key != value:
        komasAtWrongNode.append(key)

def komaInNodeOf(node):
    for key, value in koma_is_at.items():
        if value == node:
            return key
    return None

def isSolved():
    for key, value in koma_is_at.items():
        if key != value:
            return False

    return True

def getKomaAtWrongNode():
    for koma in komasAtWrongNode:
        komasAtWrongNode.popleft()
        return koma

def getEmptyNode():
    isOccupied = [False for _ in range(9)]

    for _, value in koma_is_at.items():
        isOccupied[value] = True

    emptyNode = isOccupied.index(True)
    
    return emptyNode

def isBringable(i, j):
    emptyNode = getEmptyNode()
    
    isInterconnected = graph[i][j]

    isEmptyConnected = graph[i][emptyNode] and graph[j][emptyNode]

    return isInterconnected and isEmptyConnected

prev = None
count = 0
while not isSolved():
    target = getKomaAtWrongNode()
    node = koma_is_at[target]

    if target == prev:
        print(-1)
        exit()
    prev = target

    
    if komaInNodeOf(target) is None:
        koma_is_at[target] = target
        count += 1
        continue
    if isBringable(target, node):
        koma_is_at[target], koma_is_at[komaInNodeOf(node)] = target, getEmptyNode()
        count += 2
        continue

    komasAtWrongNode.append(target)

print(count)