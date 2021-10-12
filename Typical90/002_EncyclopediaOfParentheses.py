from collections import deque

N = int(input())

if N % 2 != 0:
    exit()

candidates = []

for bit in range(1 << N):
    tmp = ""
    for i in range(N):
        if bit & (1 << i):
            tmp += "("
        else:
            tmp += ")"

    candidates.append(tmp)

candidates.sort()
stack = deque()

for item in candidates:
    stack.append(item[0])
    for i in range(1, len(item)):
        if len(stack) == 0:
            stack.append(item[i])
            continue
        if stack[-1] == "(" and item[i] == ")":
            stack.pop()
        else:
            stack.append(item[i])

    if len(stack) != 0:
        stack = deque()
        continue
    else:
        print(item)
