import sys
K = int(input())

if K % 2 == 0:
    print(-1)
    sys.exit()

if K % 5 == 0:
    print(-1)
    sys.exit()

if K % 7 == 0:
    L = 9 * K / 7
else:
    L = 9 * K

i = 1
mod = 10**i % L
while True:
    if mod == 1:
        print(i)
        sys.exit()

    mod = mod * 10 % L
    i += 1
