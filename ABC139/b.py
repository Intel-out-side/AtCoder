A, B = map(int, input().split())

taps = 1
i = 0
while taps < B:
    taps -= 1
    i += 1
    taps += A

print(i)
