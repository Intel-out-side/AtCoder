from itertools import permutations

# 順列組み合わせを試したいリスト
# WARNING: リスト内に重複がある場合使えない
# WARNING: 制約はN<=10程度
A = [1, 2, 3, 4]

for i in permutations(A):
    print(i) # -> [1, 2, 3, 4], [1, 2, 4, 3], [1, 4, 2, 3]....