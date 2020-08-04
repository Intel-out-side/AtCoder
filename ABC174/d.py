N = int(input())

c = list(input())

now = 0

count = 0

while now < len(c):
    print(c)
    if c[now] == "W":
        r = now+1
        found = False
        while r < len(c):
            if c[r] == "R":
                found = True
                break
            else:
                r += 1
        if not found:
            break
        c[now], c[r] = c[r], c[now]
        now += 1
        count += 1

    else:
        now += 1
print(count)
