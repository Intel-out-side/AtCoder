A, B, C = list(map(int, input().split()))
K = int(input())

for i in range(K):

    if A >= B:
        B *= 2

    else:
        C *= 2

if (A < B and B < C):
    print("Yes")

else:
    print("No")
