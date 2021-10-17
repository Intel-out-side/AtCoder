from collections import deque

N, Q = map(int, input().split())

A = list(map(int, input().split()))

A = deque(A)

for i in range(Q):
    T, x, y = map(int, input().split())

    if T == 1:
        A[x-1], A[y-1] = A[y-1], A[x-1]
    elif T == 2:
        tmp = A.pop()
        A.appendleft(tmp)
    else:
        print(A[x-1])