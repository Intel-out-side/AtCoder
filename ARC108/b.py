from collections import deque

N = int(input())
s = input()

stack = deque()

cnt = 0
now = 0
while now < N:

    if s[now] == "f":
        stack.append("f")
        now += 1

    elif s[now] == "o":
        if stack and stack[-1] == "f":
            stack.pop()
            stack.append("fo")
        else:
            stack.append("o")
        now += 1

    elif s[now] == "x":
        if stack and stack[-1] == "fo":
            cnt += 1
            stack.pop()
        now += 1

    else:
        stack.append(s[now])
        now += 1

ans = N - cnt*3
print(ans)
