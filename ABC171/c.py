N = int(input())

ans = ""
while N > 0:

    N -= 1

    q, r = N//26, N%26

    ans += chr(ord("a") + r)

    N = q

print(ans[::-1])
