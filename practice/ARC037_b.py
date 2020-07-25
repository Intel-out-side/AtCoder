N, M = list(map(int, input().split()))

connections = [[0 for _ in range(N)] for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(M):
    v1, v2 = list(map(int, input().split()))

    connections[v1-1][v2-1] = 1
    connections[v2-1][v1-1] = 1

def dfs(i, j):


for i in range(N):
    for j in range(i+1, N):

        if connections[i][j] == 0:
            continue

        dfs(i)
