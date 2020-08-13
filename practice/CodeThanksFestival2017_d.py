import heapq
N, K = map(int, input().split())

A, B = [0]*N, [0]*N

timesUsed = [0 for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

priorityQueue = [(A[i], i) for i in range(N)]
heapq.heapify(priorityQueue)
# print(priorityQueue)
ans = 0
for i in range(K):

    machineNow = heapq.heappop(priorityQueue)
    machineIndex = machineNow[1]
    ans += machineNow[0]
    timesUsed[machineNow[1]] += 1

    heapq.heappush(priorityQueue, (A[machineIndex] + timesUsed[machineIndex]*B[machineIndex], machineIndex))


print(ans)
