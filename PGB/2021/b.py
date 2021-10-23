X = input()
N = len(X)

ans = ""

for i in range(N):
    
    if X[i] == "0":
        ans = ans + "1"
    else:
        ans = ans + X[i]

print(ans)