from collections import defaultdict, deque

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)

print(res)
ans = ""
for item in res:
    ans += str(item)