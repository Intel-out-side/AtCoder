S = input()

N = len(S)

ans = 0
for i in range(2**(N-1)):
    tmp = S[0]
    for j in range(len(S)-1):
        flag = (i >> j) & 1

        if flag:
            tmp += "+" + S[j+1]
        else:
            tmp += S[j+1]

    num = list(map(int, tmp.split("+")))
    ans += sum(num)

print(ans)
