n = int(input())

num = n // 1000

if n % 1000 == 0:
    pass
else:
    num += 1

ans = 1000 * num - n

print(ans)
