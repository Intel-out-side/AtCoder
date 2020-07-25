S = input()
N = len(S)

for i in range(2**(N-1)):
    tmp = int(S[0])
    sentence = S[0]

    for j in range(N-1):
        flag = (i >> j) & 1

        if flag: # +の場合
            tmp += int(S[j+1])
            sentence += "+" + S[j+1]
        else:
            tmp -= int(S[j+1])
            sentence += "-" + S[j+1]

    if tmp == 7:
        print(sentence + "=7")
        exit()
