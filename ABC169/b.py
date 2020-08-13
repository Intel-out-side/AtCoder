N = int(input())
A = list(map(int, input().split()))

if A.count(0) > 0:
    print(0)
    exit()

ans = 1
for i in range(N):

    if ans * A[i] > 10**18:
        print(-1)
        exit()

    ans *= A[i]

print(ans)
