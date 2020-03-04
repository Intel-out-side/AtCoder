N = int(input())
strs = []

for i in range(N):
    strs.append(input())
count = {}

for i in range(N):
    if strs[i] not in count.keys():
        count[strs[i]] = 1
    elif strs[i] in count.keys():
        count[strs[i]] += 1

sorted_count = {k: v for k, v in sorted(count.items(), key = lambda x: x[1], reverse=True)}
max_count = list(sorted_count.values())[0]
max_items = []
for k, v in sorted_count.items():
    if (v == max_count):
        max_items.append(k)

max_items = sorted(max_items)

for item in max_items:
    print(item)
