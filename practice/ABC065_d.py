import heapq
V = int(input())

cord = [0] * V

for i in range(V):
    x, y = map(int, input().split())
    cord[i] = (x, y)

isUsed = [False for _ in range(V)]
isUsed[0] = True

res = 0
pq = []
heapq.heapify(pq)

sx, sy = cord[0]

for i in range(1, V):
    x, y = cord[i]
    cost = min(abs(sx - x), abs(sy - y))
    heapq.heappush(pq, (cost, i))


while True:
    v = -1
    if pq:
        cost, v = heapq.heappop(pq)

    if v == -1:
        break

    if not isUsed[v]:
        res += cost
        isUsed[v] = True

print(res)
