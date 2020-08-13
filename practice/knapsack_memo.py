N, W = list(map(int, input().split()))

value = [0]*N
weight = [0]*N

memo = [[None for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    v, w = list(map(int, input().split()))
    value[i], weight[i] = v, w

def search(i, u):
    if i == N:
        return 0

    if memo[i][u] is not None:
        return memo[i][u]

    else:
        if u < weight[i]:
            memo[i][u] = search(i+1, u)
            return memo[i][u]

        else:
            res1 = search(i+1, u) #i番目を使わない場合
            res2 = search(i+1, u - weight[i]) + value[i] #i番目を使う場合

            memo[i][u] = max(res1, res2)

            return max(res1, res2)

print(search(0, W))
