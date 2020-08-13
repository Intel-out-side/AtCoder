N, X, Y = map(int, input().split())

distCount = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        minDist = min(abs(j-i), abs(X-i)+1+abs(j-Y), abs(Y-i)+1+(j-X))
        distCount[minDist] += 1

for i in range(1, N):
    print(distCount[i])
