X = int(input())

while True:
    isDivisible = False
    divider = 2
    while not isDivisible or divider < X:
        isDivisible = (X % divider == 0)

        if isDivisible:
            break
        else:
            divider += 1

    if divider == X:
        break
    else:
        X += 1

print(X)
