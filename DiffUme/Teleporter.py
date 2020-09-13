N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x:x-1, A))

visited = [False for _ in range(N)]
visited[0] = True
pattern = [0]
x = 0
start = 0
patternBegin = 0
while True:
    x = A[x]
    if visited[x]:
        patternBegin = x
        break
    pattern.append(x)
    visited[x] = True

# print(pattern)
patternBeginIndex = pattern.index(patternBegin)
beforeLoop = pattern[0:patternBeginIndex]
repeat = pattern[patternBeginIndex:]
# print(beforeLoop, repeat)

if len(pattern) > K:
    print(pattern[K]+1)
else:
    ans = repeat[(K - len(beforeLoop))%len(repeat)]
    # print(pattern)
    print(ans+1)
