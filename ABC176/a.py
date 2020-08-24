N, X, T = map(int, input().split())

ans = (N // X) * T

if N % X == 0:
    print(ans)
    exit()

else:
    ans += T
    print(ans)
