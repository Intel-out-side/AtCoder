N = int(input())
s = {}
for i in range(N):
    text = input()
    if not (text in s.keys()):
        s[text] = 1
    else:
        s[text] += 1

M = int(input())
t = dict()
for i in range(M):
    text = input()
    if not (text in t.keys()):
        t[text] = 1
    else:
        t[text] += 1

for key in s.keys():
    if key not in t.keys():
        t[key] = 0


maxVal = 0
for key in s.keys():
    maxVal = max(maxVal, s[key] - t[key])

print(maxVal)
