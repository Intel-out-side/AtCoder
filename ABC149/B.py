A, B, K = map(int, input().split())

if 0 <= K < A:
    A -= K
elif A <= K <= A + B:
    B -= (K - A)
    A = 0
else:
    A = 0
    B = 0

print(A, B)
