N, M = map(int, input().split())

toys = [[0 for _ in range(N+5)] for _ in range(M)]

for i in range(N):
    t = int(input())
    toys[t-1][i+1] = 1

#累積和を考える
for i in range(M):
    for n in range(1, N+5):
        toys[i][n] += toys[i][n-1]

dp  = [float("inf")] * (1<<M)
dp[0] = 0
queuedToys = [0]*(1<<M)

for S in range(1<<M):
    #ぬいぐるみの種類に関して探索
    for i in range(M):
        #i種類目のぬいぐるみをすでに詰めているならcontinue
        if ((S >> i) & 1): continue

        nextState = S | (1<<i)
        queuedToys[nextState] = queuedToys[S] + toys[i][-1]
        numOfToysNext = queuedToys[nextState]
        numOfToysNow = queuedToys[S]

        toysToMove = toys[i][-1] - (toys[i][numOfToysNext] - toys[i][numOfToysNow])
        dp[nextState] = min(dp[nextState], dp[S]+toysToMove)

ans = dp[(1<<M)-1]
print(ans)
