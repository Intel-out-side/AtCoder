factorial = [] #階乗を事前に前計算した配列

def C(n, r):
    return factorial[n] // (factorial[r] * factorial[n-r])

#n個の区別不可なボールをr個の区別可能な箱に入れる
#-> n + (k-1) あるスロットの中からn個選ぶ
pattern = C(n + k - 1, n)


#n個の区別不能なボールをk個のグループに分ける (k=2なら仕切りはk-1個で良い)
#各ボールの右端に仕切りを置いてグループ分けすると仮定すると
pattern = C(n-1, k-1)
