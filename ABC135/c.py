N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

allMonsters = sum(A)

defeatMonsters = 0
for i in range(N):

    if A[i] <= B[i]:
        defeatMonsters += A[i]
        B[i] -= A[i]

        if A[i+1] >= B[i]:
            defeatMonsters += B[i]
            A[i+1] -= B[i]
        else:
            defeatMonsters += A[i+1]
            A[i+1] = 0

    else:
        defeatMonsters += B[i]
        B[i] = 0

print(defeatMonsters)
# print(A)
