from itertools import permutations
#O(10^8)くらい？

n = int(input())
k = int(input())

cards = [0]*n
for i in range(n):
    cards[i] = input()

candidates = []
ans = 0
for root in permutations(cards, k):
    root = list(root)

    num = ""
    for letter in root:
        num += letter
    num = int(num)

    if not num in candidates:
        ans += 1
        candidates.append(num)

print(ans)
