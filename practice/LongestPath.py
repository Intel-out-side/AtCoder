import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

#f(x) := xを始点とする最長経路
# -> xが葉の時：0
# -> そうでないとき：f(y)+1

memo = [None for _ in range(N)]
visited = [False for _ in range(N)]

def f(now:int) -> int:
    if memo[now] is not None:
        return memo[now]

    fans = 0
    for adj in graph[now]:
        fans = max(fans, f(adj)+1)

    memo[now] = fans
    return fans

ans = 0
for i in range(N):
    longest = f(i)
    ans = max(ans, longest)

print(ans)
