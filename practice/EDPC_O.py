N = int(input())

matches = [0] * N

MOD = 10**9 + 7

for i in range(N):
    matches[i] = list(map(int, input().split()))

V = 1 << N

dp = [[0 for _ in range(V+1)] for _ in range(N+5)]
dp[0][0] = 1

for men in range(N):
    #bitが立っている:すでにマッチング済み
    #bitが立っていない：マッチングしていない
    for S in range(V):
        #もし
        if dp[men][S] == 0:
            continue

        for women in range(N):
            if ((S >> women) & 1) == 0 and matches[men][women] == 1:
                dp[men+1][S | (1 << women)] += dp[men][S]
                dp[men+1][S | (1 << women)] %= MOD

ans = (dp[N][V-1] + MOD) % MOD
print(ans)
