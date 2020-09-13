N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

color = [0 for _ in range(N)]
color[0] = 1

def dfs(prev:int, now:int):

    for adj in graph[now]:
        if color[adj] == color[now]:
            return False

        if color[adj] == 0 and prev != adj:
            color[adj] = -1 * color[now]
            return dfs(now, adj)

    return True

ans = dfs(-1, 0)
print(ans)
