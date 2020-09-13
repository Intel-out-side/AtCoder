import itertools as itr
N, M, Q = map(int, input().split())
req = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1;
    req.append((a, b, c, d))


ans = -1
for pattern in itr.combinations_with_replacement(range(1, M+1), N):
    A = pattern
    tmp = 0
    for reqirements in req:
        a, b, c, d = reqirements
        if A[b] - A[a] == c:
            tmp += d

        ans = max(ans, tmp)

print(ans)
