a, b, c = map(int, input().split())

num = a
den = c**b

if num < den:
    print("Yes")
else:
    print("No")