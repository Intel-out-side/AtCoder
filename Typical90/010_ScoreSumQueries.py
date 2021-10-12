from collections import defaultdict

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
N = int(input())

Class1 = [0] * N
Class2 = [0] * N

for i in range(N):
    c, p = map(int, input().split())

    if c == 1:
        Class1[i] = p
    else:
        Class2[i] = p

C1_acum = AccumulatedSum(Class1)
C2_acum = AccumulatedSum(Class2)

Q = int(input())
ans1, ans2 = [], []

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    ans1.append(C1_acum.getSumIn(l, r))
    ans2.append(C2_acum.getSumIn(l, r))


for a, b in zip(ans1, ans2):
    print(a, b)