N, M = map(int, input().split())

#問題Pに関して複数考えられるとり方のうち、高橋：最適解(区間スケジューリング)で青木：他の何か　になっている
#よって、M<0になるようなとり方は存在しない。

if M < 0:
    print(-1)
    exit()

#この場合、高橋1で青木1しか無いので何でもいい
if N == 1 and M == 0:
    print(1, 2)
    exit()

if N - M - 1 <= 0:
    print(-1)
    exit()

if M >= 0:
    x = 2
    for i in range(M+1):
        print(x, x+1)
        x += 2

    print(1, x)
    x += 1
    rest = (N - M - 2)

    for j in range(rest):
        print(x, x+1)
        x += 2
