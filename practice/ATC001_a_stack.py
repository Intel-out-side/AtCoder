import sys
from collections import deque
H, W = list(map(int, input().split()))

city = []

for i in range(H):
    city.append(list(input()))


def dfs_stack(i, j):

    now = (i, j)

    stack = deque()
    stack.append(now)

    while len(stack) > 0:
        
