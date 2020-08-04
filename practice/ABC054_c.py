import copy
N, M = list(map(int, input().split()))

g = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))

    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = [False for _ in range(N)]

def dfs(now, prev, vis):
    visited_copy = copy.copy(vis) #参照渡しなのでコピーが必要
    visited_copy[now] = True
    all_visited = True

    for is_node_visited in visited_copy:
        if not is_node_visited:
            all_visited = False

    if all_visited:
        return 1
    #終了条件を忘れずに

    counter = 0
    for adj in g[now]:
        if prev == adj:
            continue

        if visited_copy[adj]:
            continue
        counter += dfs(adj, now, visited_copy)

    return counter

ans = dfs(0, -1, visited)
print(ans)
