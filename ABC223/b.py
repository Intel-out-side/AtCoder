S = input()
N = len(S)

S_min = S
S_max = S

for i in range(N):
    S_new = S[i:N] + S[0:i]

    # print(S_new)

    if S_max < S_new:
        S_max = S_new

    if S_min > S_new:
        S_min = S_new

print(S_min)
print(S_max)