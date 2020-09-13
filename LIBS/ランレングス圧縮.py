def runLengthEncoding(s:str) -> list:
    """
    ランレングス圧縮します。リスト内に(文字,個数)の形でカウントを収納して
    Returnします。見ての通りO(N)です。
    """
    l = []
    N = len(s)
    count = 1
    char = s[0]
    for i in range(1, N):
        if char != s[i]:
            tmp = (char, count)
            l.append(tmp)

            char = s[i]
            count = 1

        elif char == s[i]:
            count += 1

    l.append((char, count))

    return l


if __name__ == "__main__":
    S = "LLLRRRLRLRLRRRRLLLLL"

    print(runLengthEncoding("LR"))
