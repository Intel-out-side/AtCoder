N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum, B_sum = 0, 0

for i in range(N):
    A_sum += A[i]
    B_sum += B[i]

if A_sum > B_sum:
    print("A")
elif A_sum == B_sum:
    print("same")
else:
    print("B")
    