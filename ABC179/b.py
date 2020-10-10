N = int(input())

D1, D2 = [0] * N, [0] * N

for i in range(N):
    a, b = map(int, input().split())

    D1[i], D2[i] = a, b

for i in range(2, N):

    if D1[i-2] == D2[i-2] and D1[i-1] == D2[i-1] and D1[i] == D2[i]:
        print("Yes")
        exit()

print("No")
