A, B, C, D = map(int, input().split())

if C <= A <= D or A <= C <= B:
    print("Yes")
else:
    print("No")
