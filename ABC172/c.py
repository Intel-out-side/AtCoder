import sys
N, M, K = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

time = 0
a_index, b_index = 0, 0
num = 0
while time <= K:
    if a_index == len(A) and b_index == len(B):
        print(num)
        sys.exit()

    elif a_index == len(A) and b_index < len(B): #Aがもうない場合
        time += B[b_index]
        num += 1
        b_index += 1
    elif a_index < len(A) and b_index == len(B):
        time += A[a_index]
        num += 1
        a_index += 1
    else:
        if A[a_index] <= B[b_index]:
            time += A[a_index]
            num += 1
            a_index += 1
        else:
            time += B[b_index]
            num += 1
            b_index += 1


print(num-1)
