N = int(input())

A = list(map(int, input().split()))

max_A = max(A)

max_deg = -1
ans = 2
for k in range(2, max_A+1):
    deg_of_k = 0
    for a in A:

        if a % k == 0:
            deg_of_k += 1

    if deg_of_k >= max_deg:
        max_deg = deg_of_k
        ans = k

print(ans)
