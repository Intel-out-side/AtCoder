import heapq
N = int(input())
L = list(map(int, input().split()))

ans = 0
priorityQueue = L.copy()
heapq.heapify(priorityQueue)
print(priorityQueue)

while len(priorityQueue) > 1:
    l1 = heapq.heappop(priorityQueue)
    l2 = heapq.heappop(priorityQueue)

    ans += (l1 + l2)
    heapq.heappush(priorityQueue, l1+l2)

print(ans)
