N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ownPlays = ""

for i in range(N):
    if i - K >= 0:
        playsBackToKth = ownPlays[i - K]
        # if opponent plays s
        if T[i] == "s":
            if playsBackToKth == "r":
                ownPlays += "s"
            else:
                ownPlays += "r"

        elif T[i] == "p":
            if playsBackToKth == "s":
                ownPlays += "p"
            else:
                ownPlays += "s"

        elif T[i] == "r":
            if playsBackToKth == "p":
                ownPlays += "r"
            else:
                ownPlays += "p"
    else:
        if T[i] == "s":
            ownPlays += "r"
        elif T[i] == "p":
            ownPlays += "s"
        elif T[i] == "r":
            ownPlays += "p"

sum = 0
for i in range(N):
    if ownPlays[i] == "p" and T[i] != "p":
        sum += P
    elif ownPlays[i] == "s" and T[i] != "s":
        sum += S
    elif ownPlays[i] == "r" and T[i] != "r":
        sum += R

print(sum)
