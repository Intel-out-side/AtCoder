# 配列を二分探索できる時は、bisectを使った方がいい！
import bisect
A = [1, 2, 3, 4, 5]

left_idx = bisect.bisect(A, 3) # -> 2


#単調増加関数で２分探索する場合
def func(a):
    return a

li = [] #ソートされたリスト内で二分探索する場合
#同じ値が存在する場合は要注意な気がする

left = 0 # 左端
right = 10**9 # 右端
mid = None
found = False

#終了したときに left|見つけたい値|rightの様に挟まれる
#WARNING: 探索区間内に見つけたい値が無い場合は例外処理が必要
#WARNING: リストの先頭が条件を満たす値になっている場合例外処理が必要
while left+1 < right:
    mid = (left + right)//2

    if f(mid) == 0:
        found = True
        break
    elif f(mid) < 0:
        left = mid
    else:
        right = mid

if found:
    ans = f(mid)
else:
    #f(left)とf(right)の間に見つけたい値が存在する