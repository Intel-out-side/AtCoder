N = int(input())
a = list(map(int, input().split()))

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
        if left <= 0:
            return self.accumulated_sum[right]

        return self.accumulated_sum[right] - self.accumulated_sum[left-1]


dp = [[0 for _ in range(N+5)] for _ in range(N+5)]
#dp[i][j] := 区間[i,j)問題の制約に沿って合体させる時のコストの最小値

for i in range(N+5):
    dp[i][i] = 0

acum = AccumulatedSum(a)

ans = 0
for length in range(2, N+1):
    i = 0
    while i + length <= N:
        j = i + length
        ret = float("inf")
        for k in range(i+1, j):
            ret = min(ret, dp[i][k] + dp[k][j])

        dp[i][j] = ret + acum.getSumIn(i, j-1)
        i += 1

# print(dp)
ans = dp[0][N]
print(ans)
