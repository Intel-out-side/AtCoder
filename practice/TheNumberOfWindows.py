N, Q = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

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


acSum = AccumulatedSum(a)

for i in range(Q):
    q = x[i]

    s = 0
    t = 0
    ans = 0
    while t < N:
        while acSum.getSumIn(s, t) <= q:
            t += 1
            if t == N:
                break

        ans += ((t-1) - s) + 1
        s = t

    print(ans)
