N = int(input())
A = list(map(int, input().split()))

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

#max distance from zero
md = [0] * N
md[0] = A[0]
asum = AccumulatedSum(A)
for i in range(1, N):
    md[i] = max(md[i-1], asum.getSumIn(0, i))


now = 0
ans = 0
for i in range(N):
    ans = max(ans, now + md[i])
    now += asum.getSumIn(0, i)

print(ans)
