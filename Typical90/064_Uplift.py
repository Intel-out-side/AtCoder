N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = [0]*(N-1)

for i in range(N-1):
    D[i] = A[i+1] - A[i]

now = 0
for item in D:
    now += abs(item)

ans = []
for q in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    
    if l > 0:
        Dl_prev = D[l-1]
        D[l-1] += v
        
        now += abs(D[l-1]) - abs(Dl_prev)
    
    if r < N-1:
        Dr_prev = D[r]
        D[r] -= v

        now += abs(D[r]) - abs(Dr_prev)
    
    ans.append(now)

for item in ans:
    print(item)