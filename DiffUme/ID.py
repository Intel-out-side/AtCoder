from collections import defaultdict
N, M = map(int, input().split())

cities = defaultdict(list)

P, Y = [0]*M, [0]*M

for i in range(M):
    p, y = map(int, input().split())

    cities[p].append((i, y))

prefs = cities.keys()

for pref in prefs:
    cities[pref].sort(key=lambda x:x[1])

# print(cities)

ids = defaultdict(str)

for pref in prefs:
    i = 1
    for item in cities[pref]:
        cityNum, birthYear = item

        prefStr = str(pref)
        ans = "0" * (6 - len(prefStr)) + prefStr

        cityNumStr = str(i)
        ans = ans + "0" * (6 - len(cityNumStr)) + cityNumStr
        i += 1
        ids[cityNum] = ans

ids = sorted(ids.items(), key=lambda x:x[0])

for item in ids:
    print(item[1])
