N = int(input())

ac, wa, tle, re = 0, 0, 0, 0
for i in range(N):
    tmp = input()
    if tmp == "AC":
        ac += 1
    elif tmp == "WA":
        wa += 1
    elif tmp == "TLE":
        tle += 1
    elif tmp == "RE":
        re += 1

print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))
