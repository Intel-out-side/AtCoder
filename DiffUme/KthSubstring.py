import heapq
from collections import defaultdict
s = input()
K = int(input())
N = len(s)

cand = []
heapq.heapify(cand)

used = defaultdict(int)


for i in range(N):
    for j in range(i+1, min(i+K+1, N+1)):
        sub = s[i:j]
        if used[sub] == 0:
            used[sub] += 1
            heapq.heappush(cand, sub)

ans = None
for i in range(K):
    ans = heapq.heappop(cand)

print(ans)

#全列挙するとO(N^2 logN)で終わると思ったけど実際は文字列の比較でO(N)かかるので
#全部でO(N^3logN)かかってしまう

#K番目の辞書順の部分文字列は|s|<=Kが必ず成り立つことを利用して二番目のループを
#+K文字目までに限定すればよい
