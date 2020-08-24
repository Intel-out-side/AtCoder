N = int(input())
P = list(map(int, input().split()))

isPossible = True
for k in range(N-1):
    if P[k] > P[k+1]:
        isPossible = False
if isPossible:
    print("YES")
    exit()


for i in range(N):
    for j in range(i+1, N):
        newList = P.copy()
        newList[i], newList[j] = newList[j], newList[i]
        isPossible = True
        for k in range(N-1):
            if newList[k] > newList[k+1]:
                isPossible = False

        if isPossible:
            print("YES")
            exit()
print("NO")
