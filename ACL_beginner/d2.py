from atcoder.segtree import SegTree

N, K = map(int, input().split())
maxA = 300000

segTree = SegTree(op=lambda x,y:max(x,y), e=0, v=maxA+1)
#op : operator, e : 単位元, v :　配列のサイズ

for i in range(N):
    x = int(input())
    l = max(0, x - K)
    r = min(x + K, maxA)
    now = segTree.prod(l, r+1) + 1
    segTree.set(x, now)

ans = segTree.prod(0, maxA)
print(ans)
