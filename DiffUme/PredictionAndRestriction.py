N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
wins = {"p":"s", "r":"p", "s":"r"}
points = {"p":S, "r":P, "s":R}
hands = []

ans = 0
for i in range(N):
    if i - K < 0:
        hands.append(wins[T[i]])
        ans += points[T[i]]
    else:
        if hands[i-K] == wins[T[i]]:
            #あいこにするしか無い時
            hands.append(T[i])
        else:
            #勝てる時
            hands.append(wins[T[i]])
            ans += points[T[i]]
print(ans)
