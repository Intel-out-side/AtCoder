import bisect

from pkg_resources import safe_extra
N, K = map(int, input().split())

array = [None] * N

for i in range(N):
    p1, p2, p3 = map(int, input().split())
    array[i] = (i, (p1+p2+p3))

array = sorted(array, key=lambda x:x[1])

I = [x[0] for x in array]
P = [x[1] for x in array]

ans = [None] * N

for i in range(N):

    now = P[i]

    left = bisect.bisect_left(P, now+300)
    right = bisect.bisect_right(P, now+300)

    if right >= N:
        ans[I[i]] = "Yes"
    elif N-right < K:
        ans[I[i]] = "Yes"
    else:
        ans[I[i]] = "No"
         
for item in ans:
    print(item)