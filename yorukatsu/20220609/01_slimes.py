from collections import deque

N = int(input())
S = input()

stack = deque()

stack.append("-1")

for i in range(N):
    now = S[i]

    if stack[-1] == now:
        continue
    else:
        stack.append(now)

ans = len(stack) - 1
print(ans)