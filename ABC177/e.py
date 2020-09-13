import math
N = int(input())
A = list(map(int, input().split()))
m = [False for _ in range(N)]
def factorize(n):
    i = 2
    factors = set()
    while i**2 <= n:
        if n % i != 0:
            i += 1
            continue

        while n % i == 0:
            n = n // i
            factors.add(i)
        i += 1

    if n != 1:
        factors.add(n)

    return factors

isSetWise = False
gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])
if gcd == 1:
    isSetWise = True

isPairWise = True
g = factorize(A[0])
for i in range(1, N):
    f = factorize(A[i])

    if not g.isdisjoint(f):
        isPairWise = False
        break
    g = g | f

if isPairWise:
    print("pairwise coprime")
    exit()

if isSetWise:
    print("setwise coprime")
    exit()

print("not coprime")
