import itertools
N = int(input())
robots = []
for _ in range(N):
    robots.append(list(map(int, input().split())))

print(robots)
Xn = robots[N-1][0]

all_robots = [i for i in range(N)]

combinations_okay = []
sums = []
for x in range(1, N+1):
    all_combinations = list(itertools.combinations(all_robots, x))
    print(all_combinations)

    sum = 0
    for item in all_combinations:
        isPlacable = True
        for i in range(len(item) - 1):
            if robots[item[i]][0] + robots[item[i]][1] > robots[item[i+1]][0] - robots[item[i+1]][1]:
                isPlacable = False

        if isPlacable:
            combinations_okay.append(len(item))

print(combinations_okay)
print(max(combinations_okay))
