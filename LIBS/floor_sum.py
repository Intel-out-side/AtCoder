"""
Σ(i:0->N-1) floor((A*i+B)/M)を返す関数
O(log(A+B+N+M))でできる
"""
def floor_sum(n: int, m: int, a: int, b: int) -> int:
    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans
