N, M = list(map(int, input().split()))

#隣接リスト表現
connection = [[] for _ in range(N)]

for i in range(M):
    u, v = list(map(int, input().split()))
    connection[u-1].append(v-1)
    connection[v-1].append(u-1)

#すでに訪問されたかどうか
visited = [False] * N

#木の個数のカウンター
counter = 0

def dfs(now, prev):
    global flag
    visited[now] = True

    for next in connection[now]:
        if next != prev:
            if visited[next] == True:
                flag = False
            else:
                dfs(next, now)

for i in range(N):
    if not visited[i]:
        flag = True
        dfs(i, -1)
        if flag:
            counter += 1

print(counter)
