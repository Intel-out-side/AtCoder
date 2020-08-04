N, K = list(map(int, input().split()))
K -= 1
A = list(map(int, input().split()))

index = 0
left = A[index]

for i in range(K+1, N):

    if A[index] < A[i]:
        print("Yes")
    else:
        print("No")

    index += 1
