I = input().split()
N = int(I[0])
S = I[1]

class AccumulatedSum:
    """
    累積和を勝手に計算します。
    0-indexedなので注意
    """
    def __init__(self, A:list):
        self.N = len(A)
        self.accumulated_sum = A.copy()

        for i in range(1, self.N):
            self.accumulated_sum[i] += self.accumulated_sum[i-1]

    def getSumIn(self, left:int, right:int) -> int:
        """
        [l, r]区間の和を計算します。左右端も含みます。
        """
        if left == 0:
            return self.accumulated_sum[right]

        return self.accumulated_sum[right] - self.accumulated_sum[left-1]


A = [0] * N
T = [0] * N
C = [0] * N
G = [0] * N

for i in range(N):
    if S[i] == "A":
        A[i] = 1

    if S[i] == "T":
        T[i] = 1

    if S[i] == "C":
        C[i] = 1

    if S[i] == "G":
        G[i] = 1

Aacc = AccumulatedSum(A)
Tacc = AccumulatedSum(T)
Cacc = AccumulatedSum(C)
Gacc = AccumulatedSum(G)

ans = 0

for i in range(N):
    for j in range(i, N):

        if Aacc.getSumIn(i, j) == Tacc.getSumIn(i, j) and Cacc.getSumIn(i, j) == Gacc.getSumIn(i, j):
            ans += 1
print(ans)
