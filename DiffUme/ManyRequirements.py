N, M, Q = map(int, input().split())
requirements = [0]*Q
for i in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1
    requirements[i] = (a, b, c, d)

requirements.sort(key=lambda x:x[3], reverse=True)
print(requirements)

taken = [False for i in range(N)]
ans = 0
A = [-1 for i in range(N)]

for i in range(Q):
    a, b, c, d = requirements[i]
    print(A)
    if not taken[b]:
        if not taken[a]:
            if A[a-1] + c <= M:
                if a == 0:
                    A[a] = 1
                    A[b] = A[a] + c
                    taken[a] = taken[b] = True
                    ans += d
                    continue
                A[a] = A[a-1]
                A[b] = A[a] + c
                taken[a] = True
                taken[b] = True
                ans += d
            else:
                pass
        if taken[a]:
            if A[a] + c <= M:
                A[b] = A[a] + c
                taken[b] = True
                ans += d
            else:
                pass
    if taken[b]:
        if not taken[a]:
            if A[b] - c >= 1:
                A[a] = A[b] - c
                taken[a] = True
                ans += d
            else:
                pass
        else:
            pass

print(A)
print(ans)
