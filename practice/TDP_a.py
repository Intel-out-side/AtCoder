N = int(input())
p = list(map(int, input().split()))
p = [0] + p
maxPoint = sum(p)


def search(i, sumPoint, now):
    # global memo
    if i > N:
        return 0

    if sumPoint == now + p[i]:
        return 1

    if memo[i][now] > -1:
        return memo[i][now]
    else:
        res1 = search(i+1, sumPoint, now+p[i])
        res2 = search(i+1, sumPoint, now)
        memo[i][now] = (res1 or res2)
        return res1 or res2

isPossible = [False] * (maxPoint+1)
for i in range(maxPoint+1):
    memo = [[-1 for _ in range(maxPoint+1)] for _ in range(N+1)]
    res = search(0, i, 0)
    print(memo)

    isPossible[i] = res

print(isPossible.count(True))
