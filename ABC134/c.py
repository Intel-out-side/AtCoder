import heapq
N = int(input())
A = [0]*N

maxVal = -1
for i in range(N):
    A[i] = int(input())
    maxVal = max(maxVal, A[i])

secondMax = -1
maxIndex = A.index(maxVal)
A[maxIndex] = -1
secondMax = max(A)
A[maxIndex] = maxVal

for i in range(N):
    if A[i] == maxVal:
        print(secondMax)
    else:
        print(maxVal)
