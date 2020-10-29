from collections import Counter
S = input()
N = len(S)

#Tkをk+1文字目以降の数字を10進数表記したときの数字であるとする
T = [0] * (N+1)
T[N] = int(S[N-1])

fac = 10
for i in range(N-2, -1, -1):
    #N-1スタート
    T[i+1] = int(S[i])*fac + T[i+2]
    T[i+1] %= 2019
    fac = fac * 10 % 2019

count = Counter(T)

ans = 0
for val in count.values():
    ans += val * (val-1) // 2

print(ans)
