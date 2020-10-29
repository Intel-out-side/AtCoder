n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

if n == 2:
    print(*a)
    exit()

l = a[0]

if l % 2 == 1:
    desirable = l//2 + 1
    r = a[0]

    for item in a:
        if abs(item - desirable) < abs(r - desirable):
            r = item

    print(l, r)

else:
    desirable = l//2
    r = a[0]
    for item in a:
        if abs(item - desirable) < abs(r - desirable):
            r = item

    print(l, r)
