from collections import Counter

S = input()

l = Counter(S)

a = len(l.keys())

if a == 3:
    print(6)
elif a == 2:
    print(3)
else:
    print(1)