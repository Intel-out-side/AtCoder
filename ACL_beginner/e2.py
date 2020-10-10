N, Q = map(int, input().split())
S = [1 for _ in range(N)]

for _ in range(Q):
    L, R, D = map(int, input().split())
    L -= 1; R -= 1;
    S[L:R] = [9] * (R-L)*1
