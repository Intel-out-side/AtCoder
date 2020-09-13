X, Y, A, B, C = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

cand = p[0:X] + q[0:Y] + r

cand.sort(reverse=True)

ans = sum(cand[0:X+Y])
print(ans)
