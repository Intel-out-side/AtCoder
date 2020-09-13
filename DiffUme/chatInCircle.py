import math
N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)

ans = A[0]
for i in range(1, N-1):
    # print(math.ceil(i/2), A[math.ceil(i/2)])
    ans += A[math.ceil(i/2)]
print(ans)
