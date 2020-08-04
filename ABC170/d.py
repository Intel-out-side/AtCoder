N = int(input())
A = list(map(int, input().split()))
A.sort()

maxVal = max(A)+1
isPrime = [0] * maxVal
isDuplicate = [0] * maxVal
isDivisible = [0] * maxVal

for i in range(len(A)):
    if not isDivisible[A[i]]:
        isPrime[A[i]] += 1

        j = 2
        while A[i] * j < maxVal:
            isDivisible[A[i] * j] = 1

            j += 1

ans = isPrime.count(1)

print(ans)
