from collections import defaultdict
N = int(input())

A = list(map(int, input().split()))

pair_pos = defaultdict(list)
pair_dist = defaultdict(int)

for i in range(2*N):
    pair_pos[A[i]].append(i)

for i in range(N):
    pair_dist[i+1] = pair_pos[i+1][1] - pair_pos[i+1][0] - 1

dist_count = defaultdict(int)

for _, value in pair_dist.items():
    dist_count[value] += 1

for k in range(1, 2*N - 1):
    dist_count[k] += dist_count[k-1]

for k in range(2*N - 1):
    print(dist_count[k])