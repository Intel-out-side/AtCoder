from collections import defaultdict
import _ctypes
class Train:
    def __init__(self, i):
        self.num = i
        self.head = None
        self.tail = None

N, Q = map(int, input().split())

trains = dict()
for i in range(N):
    trains[i] = Train(i)

ans = []
for _ in range(Q):
    query = list(map(int, input().split()))

    #unite trains
    if query[0] == 1:
        x, y = query[1], query[2]
        x -= 1
        y -= 1
        trains[x].tail = trains[y]
        trains[y].head = trains[x]

    elif query[0] == 2:
        x, y = query[1], query[2]
        x -= 1
        y -= 1
        
        trains[x].tail = None
        trains[y].head = None

    else:
        x = query[1]-1
        now = trains[x]
        while now.head is not None:
            now = now.head

        line = []
        n = 0
        while True:
            line.append(now.num+1)
            n += 1
            now = now.tail

            if now is None:
                break

        ans.append([n]+line)

for item in ans:
    print(*item)