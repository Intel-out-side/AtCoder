import sys
sys.setrecursionlimit(10**7)
class SegmentTree:
    """
    単位元のメモ書き（各演算に対する単位元の対応）
    f(x,y) := x+y -> 0
    f(x,y) := x-y -> 0
    f(x,y) := x*y -> 1
    f(x,y) := gcd(x, y) -> 0
    """

    def __init__(self, size, func=lambda x,y:x+y, default=0):
        """
        size : 配列のサイズ
        func : queryの内容(e.g. 区間和ならf(x, y)=x+y)
        default : 単位元
        """
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default for _ in range(self.size*2-1)]
        self.f = func

    def update(self, i, x):
        """
        i番目の値をxに変更する。0-indexedなので注意
        """
        i = i + self.size - 1 #一番下の層の値
        self.dat[i] = x

        while i > 0:
            i = (i-1)>>1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, a, b, k=0, L=0, R=None, D):
        """
        区間[a, b]に関するクエリを処理します。
        例えばi=1,2,3に関して処理したいなら外からquery(1, 3+1)と呼ぶ必要があります。
        """
        if R is None:
            R = self.size

        #区間がかぶっていない場合
        if R <= a or b <= L:
            return

        #区間が完全に収まっている場合
        if a <= L and R <= b:
            self.dat[k] = D
            return

        else:
            lres = self.query(a, b, 2*k+1, L, (L+R)>>1, D)
            rres = self.query(a, b, 2*k+2, (L+R)>>1, R, D)

MOD = 998244353
N, Q = map(int, input().split())
segTree = SegmentTree(N, lambda x, y:)
for i in range(N):
    segTree.update(i, 1)

for i in range(Q):
