
def solve(N, S):
    ans = 0
    R, G, B = 0, 0, 0
    for i in range(N):
        if S[i] == "R":
            R += 1
        elif S[i] == "G":
            G += 1
        else:
            B += 1
    # print(R, G, B, R*G*B)
    ans = R * G * B

    dif = 1
    while dif <= N//2+1:
        idx = 0
        while idx + dif + dif < N:
            if S[idx] != S[idx + dif] and S[idx+dif] != S[idx+2*dif] and S[idx+2*dif] != S[idx]:
                ans -= 1
            idx += 1
        dif += 1
    print(ans)
if __name__ == '__main__':
    # N = 4000
    # S = 'RGBR' * 1000
    N = int(input())
    S = input()

    solve(N, S)
