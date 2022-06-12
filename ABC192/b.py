S = input()

N = len(S)
isUnreadable = True

for i in range(0, N, 2):
    if 'A' <= S[i] <= 'Z':
        isUnreadable = False

for i in range(1, N, 2):
    if 'a' <= S[i] <= 'z':
        isUnreadable = False

if isUnreadable:
    print("Yes")
else:
    print("No")
