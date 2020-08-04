import sys
N, M, K = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_accum = [0] * (N+1)
b_accum = [0] * (M+1)

for i in range(len(A)):
    a_accum[i+1] = a_accum[i] + A[i]

for j in range(len(B)):
    b_accum[j+1] = b_accum[j] + B[j]


best = 0
j = len(B)
for i in range(len(a_accum)):

    if a_accum[i] > K:
        break

    while b_accum[j] + a_accum[i] > K:
        j -= 1

    best = max(best, i+j)

print(best)
