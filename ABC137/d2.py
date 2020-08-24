import heapq
N, M = map(int, input().split())

jobs = [[] for _ in range(M+1)]

for i in range(N):
    a, b = map(int, input().split())
    if a <= M:
        jobs[M-a].append(b)

ans = 0
priorityQueue = []
heapq.heapify(priorityQueue)
for i in range(M-1, -1, -1):
    for jobValues in jobs[i]:
        heapq.heappush(priorityQueue, -1*jobValues)
    if len(priorityQueue) > 0:
        ans += heapq.heappop(priorityQueue) * (-1)

print(ans)
