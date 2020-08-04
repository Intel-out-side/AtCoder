X, Y = list(map(int, input().split()))

crane = 0
turtle = X

while turtle >= 0:

    allLegs = crane * 2 + turtle * 4
    if allLegs == Y:
        print("Yes")
        exit()

    crane += 1
    turtle -= 1

print("No")
