
def main():
    N, M = tuple(map(int, input().split()))

    digits = {}
    for i in range(M):
        s, c = tuple(map(int, input().split()))
        digits[s] = c

    num = 0

    for s, c in digits.items():
        num += 10 ** (s - 1) * c


    illegal = False
    if len(str(num)) > 1:
        if str(num)[::-1][0] == 0:
            illegal = True

    num = int(str(num)[::-1])

    length = len(str(num))

    if length >= N and not illegal:
        print(num)
    else:
        print(-1)

if __name__ == "__main__":
    main()
