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
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b


if N == 1:
    print(A[0]/2)
    exit()

if N == 2:
    ans = None
    t = (A[1]/B[1] + A[0]/B[0])/2

    if A[0]*B[1] < A[1]*B[0]:
        ans = B[0] * t
    else:
        ans = A[0] + (A[1] - B[1]*t)

    print(ans)
    exit()

T = [A[i]/B[i] for i in range(N)]
T_acum = AccumulatedSum(T)
mid = T_acum.getSumIn(0, N-1) / 2
mid_index = 0

for i in range(N):
    if T_acum.getSumIn(0, i) >= mid:
        mid_index = i
        break

if mid_index == 0:
    t = T_acum.getSumIn(0, N-1)/2

    ans = B[0] * t
    print({"{:7}".format(ans)})
    exit()

l = T_acum.getSumIn(0, mid_index-1)
r = T_acum.getSumIn(mid_index+1, N-1)

t = (T[mid_index] + r - l)/2
ans = 0
for i in range(mid_index):
    ans += A[i]
ans += B[mid_index] * t

print("{:6}".format(ans))