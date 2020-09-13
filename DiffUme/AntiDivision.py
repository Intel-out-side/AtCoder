import math
A, B, C, D = map(int, input().split())

#Cについて
divByC = 0
r = A % C
if r != 0:
    d = A + (C - r)
else:
    d = A
if d <= B:
    divByC = (B - d + 1) // C
    if (B - d + 1) % C != 0:
        divByC += 1
# print(r, d, divByC)

#Dについて
divByD = 0
r = A % D
if r != 0:
    d = A + (D-r)
else:
    d = A
if d <= B:
    divByD = (B - d + 1) // D
    if (B-d+1) % D != 0:
        divByD += 1
# print(r, d, divByD)

lcm = C * D // math.gcd(C, D)

divByBoth = 0
r = A % lcm
if r != 0:
    d = A + (lcm-r)
else:
    d = A
if d <= B:
    divByBoth = (B - d + 1) // lcm
    if (B - d + 1) % lcm != 0:
        divByBoth += 1
# print(r, d, divByBoth)

print((B - A + 1) - (divByC + divByD - divByBoth))
