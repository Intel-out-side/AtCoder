from collections import defaultdict
S = input()
T = input()
N = len(S)

pairs = defaultdict(str)

for i in range(N):
    if S[i] == T[i]:
        continue
    else:
        if pairs[S[i]] == "":
            pairs[S[i]] = T[i]
        else:
            print("No")
            exit()

print("Yes")
