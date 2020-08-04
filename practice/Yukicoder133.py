from itertools import permutations
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

all_count = 0
win_count = 0

for a in permutations(A):
    for b in permutations(B):
        a_win = 0
        b_win = 0
        for a_, b_ in zip(list(a), list(b)):
            if a_ > b_:
                a_win += 1
            elif a_ < b_:
                b_win += 1

        if a_win > b_win:
            win_count += 1
        all_count += 1

p = win_count / all_count
print(f'{p:10}')
