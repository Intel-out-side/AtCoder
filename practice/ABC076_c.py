"""
S' = ????
T= zzz
の場合、最初のケースをreturnしてしまうと
zzzaが答えになる。実際はazzzが答えなので不適。

"""
import sys
S = input()
T = input()

S_len = len(S)
T_len = len(T)

if T_len > S_len:
    print("UNRESTORABLE")
    sys.exit()

#条件１に関して
candidate = []
for i in range(0, S_len-T_len+1):

    isOkay = True
    for j in range(T_len):
        if S[i+j] == "?":
            continue

        if S[i+j] == T[j]:
            continue
        else:
            isOkay = False

    if isOkay:
        candidate.append((S[0:i] + T + S[i+T_len:]).replace("?", "a"))

if len(candidate):
    candidate.sort()
    print(candidate[0])
else:
    print("UNRESTORABLE")
