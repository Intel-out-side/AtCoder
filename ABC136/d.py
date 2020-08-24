S = input()
N = len(S)

S = [1 if S[i] == "R" else -1 for i in range(N)]
count = [0 for _ in range(N)]

for start in range(N):

    x = start
    visited = [False for _ in range(N)]
    pattern = []
    while not visited[x]:
        visited[x] = True
        pattern.append(x)
        x += S[x]
    pattern_begin = x
    pattern_begin_index = pattern.index(pattern_begin)
    # print(pattern, pattern_begin, pattern_begin_index)

    extraPart = pattern[0:pattern_begin_index]
    patternPart = pattern[pattern_begin_index:]

    # print(extraPart, patternPart)

    end_point = patternPart[0] + (10**100 - len(extraPart)) % len(patternPart)
    count[end_point] += 1

for i in range(N):
    print(count[i])
