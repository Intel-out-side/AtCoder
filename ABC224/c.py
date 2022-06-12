import math
N = int(input())

x = [0 for _ in range(N)]
y = [0 for _ in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
zentai = nCr(N, 3)

count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            xi, xj, xk = x[i], x[j], x[k]
            yi, yj, yk = y[i], y[j], y[k]
            if (x[i] == x[j]) and (x[j] == x[k]):
                count += 1
                continue

            if (y[i] == y[j]) and (y[j] == y[k]):
                count += 1
                continue

            bool1 = (y[j] - y[i])*(x[k] - x[i]) == (y[k]-y[i])*(x[j]-x[i])
            bool2 = -(y[j]-y[i])*x[j]*(x[k]-x[j]) + y[j]*(x[j]-x[i])*(x[k]-x[j]) == -(y[k]-y[j])*x[k]*(x[j]-x[i]) + y[k]*(x[k]-x[j])*(x[j]-x[i])
            if bool1 and bool2:
                count += 1
                continue

ans = zentai - count
print(ans)