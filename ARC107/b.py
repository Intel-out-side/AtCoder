N, K = map(int, input().split())

def getPattern(val):

    if val == 0:
        return 1

    if val == 1:
        return 2

    return val

ans = 0
for B in range(2, 2*N+1):
    A = K + B
    # A = K + B
    if A < 2:
        continue
    if A > 2 * N:
        continue

    if B - 2 == 0:
        ans += 1 * (A-2)
    elif B - 2 == 1:
        ans += 2 * (A-2)
    else:
        ans += (B-2) * (A-2)
    print(ans)

print(ans-1)
