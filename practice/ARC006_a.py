N = int(input())
weight = [0]*N
for i in range(N):
    weight[i] = int(input())

mountain = [float("inf")]
for i in range(N):
    mountain.sort()

    isStored = False
    for j in range(len(mountain)):
        if mountain[j] >= weight[i]:
            mountain[j] = weight[i]
            isStored = True
            break

    if not isStored:
        mountain.append(weight[i])
print(len(mountain))
