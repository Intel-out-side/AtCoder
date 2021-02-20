A, B = map(int, input().split())

max_follow = 2*A + 100

to_follow = max_follow - B

if to_follow >= 0:
    print(to_follow)
else:
    print(0)
