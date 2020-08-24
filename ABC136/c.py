N = int(input())
H = list(map(int, input().split()))

if N == 1:
    print("Yes")
    exit()

flag = True
for i in range(N-1, -1, -1):

    if H[i] >= H[i-1]:
        pass
    elif H[i] + 1 == H[i-1]:
        H[i-1] -= 1

for i in range(N-1):
    if H[i] > H[i+1]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
