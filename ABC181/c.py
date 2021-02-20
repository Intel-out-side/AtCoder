N = int(input())

x, y = [0]*N, [0]*N

for i in range(N):
    a, b = map(int, input().split())
    x[i], y[i] = a, b


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            xi, xj, xk = x[i], x[j], x[k]
            yi, yj, yk = y[i], y[j], y[k]
            if (x[i] == x[j]) and (x[j] == x[k]):
                print("Yes")
                exit()

            if (y[i] == y[j]) and (y[j] == y[k]):
                print("Yes")
                exit()



            bool1 = (y[j] - y[i])*(x[k] - x[i]) == (y[k]-y[i])*(x[j]-x[i])
            bool2 = -(y[j]-y[i])*x[j]*(x[k]-x[j]) + y[j]*(x[j]-x[i])*(x[k]-x[j]) == -(y[k]-y[j])*x[k]*(x[j]-x[i]) + y[k]*(x[k]-x[j])*(x[j]-x[i])
            if bool1 and bool2:
                print("Yes")
                exit()

print("No")
