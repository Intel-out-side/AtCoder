N = int(input())

ans = [0 for _ in range(10**4+1)]

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            val = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if val <= 10**4:
                ans[val] += 1

for i in range(1, N+1):
    print(ans[i])
