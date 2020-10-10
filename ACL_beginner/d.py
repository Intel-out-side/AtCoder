from collections import deque
N, K = map(int, input().split())

stack = deque()

for i in range(N):
    Ai = int(input())
    if i == 0:
        stack.append(Ai)
        continue

    if abs(stack[-1] - Ai) <= K:
        stack.append(Ai)

ans = len(stack)
print(stack)
print(ans)
