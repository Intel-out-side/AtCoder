from collections import defaultdict
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_dict = defaultdict(list)
B_dict = defaultdict(list)
C_dict = defaultdict(list)

for i in range(N):
    ra, rb, rc = A[i] % 46, B[i] % 46, C[i] % 46
    A_dict[ra].append(i)
    B_dict[rb].append(i)
    C_dict[rc].append(i)

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            
            if (i + j + k) % 46 == 0:
                ans += len(A_dict[i]) * len(B_dict[j]) * len(C_dict[k])

print(ans)