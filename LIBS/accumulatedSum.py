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


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    N = len(l)
    test = AccumulatedSum(l)
    print(test.accumulated_sum)
    print(test.getSumIn(0, 2))
    print(test.getSumIn(0, 0))
