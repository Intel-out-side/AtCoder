import math
N = int(input())

for a in range(1, 100):

    tmp = N - 3**a
    if tmp < 5:
        print(-1)
        exit()
    for b in range(1, 100):
        if 5**b == tmp:
            print(a, b)
            exit()

print(-1)
