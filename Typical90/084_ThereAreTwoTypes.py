N = int(input())
S = input()

prev = S[0]
arr = [1]
for i in range(1, N):
    if S[i] == prev:
        arr[-1] += 1

    else:
        prev = S[i]
        arr.append(1)

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

accum_arr = AccumulatedSum(arr)
ans = 0
arr_len = len(arr)
for i in range(arr_len):

    ans += arr[i] * accum_arr.getSumIn(i+1, arr_len-1)

print(ans)