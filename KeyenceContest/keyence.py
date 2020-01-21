import math
H = int(input())
W = int(input())
N = int(input())

L = max(H, W)

x = math.ceil(N / L)

print(x)
