N = int(input())

c = [0] * N

for i in range(N):
    val = int(input())
    c[i] = val

dp = [0 for _ in range(N)]

for i in range(N):
    
