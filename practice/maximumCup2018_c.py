import sys
sys.setrecursionlimit(10**8)
N = int(input())

graph = [None for _ in range(N)]
color = [0 for _ in range(N)]

for i in range(N):
    graph[i] = int(input()) - 1

def dfs(now, c):

    color[now] = c
    adj = graph[now]
    if color[adj] == color[now]:
        return False
    if color[adj] == 0 and dfs(adj, -c) == False:
        return False

    return True

ans = True
for i in range(N):
    if color[i] == 0:
        ans = ans and dfs(i, 1)
white = color.count(1)
maxDevil = max(white, N-white)

if ans:
    print(maxDevil)
else:
    print(-1)
