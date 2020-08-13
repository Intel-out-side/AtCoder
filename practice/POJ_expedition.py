import heapq
N = 4
L = 25
P = 10

A = [10, 14, 20, 21]
B = [10, 5, 2, 4]

A.append(L)
B.append(0)
N += 1

priorityQueue = []
heapq.heapify(priorityQueue)
#最小値しか対応していないので入力時に-1したほうが安全

ans, pos, tank = 0, 0, P

for i in range(N):
    #次に進む距離
    dist = A[i] - pos
    print(priorityQueue)

    while tank - dist < 0:
        if len(priorityQueue) == 0:
            print(-1)
            exit()

        tank += heapq.heappop(priorityQueue) * (-1)
        ans += 1

    tank -= dist
    pos = A[i]
    heapq.heappush(priorityQueue, B[i]*(-1))

print(ans)
