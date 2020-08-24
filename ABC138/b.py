N = int(input())
A = list(map(int, input().split()))

mulAll = 1
for i in range(N):
    mulAll *= A[i]

num = 0
for i in range(N):
    mulAll //= A[i]
    num += mulAll
    mulAll *= A[i]

ans = mulAll / num

print(ans)
