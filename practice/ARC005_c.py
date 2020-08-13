T = int(input())
N = int(input())

A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print("no")
    exit()

A.sort()
B.sort()

for i in range(M)
