N = int(input())
jobs = [0]*N
for i in range(N):
    a, b = map(int, input().split())
    jobs[i] = (a, b)

jobs.sort(key=lambda x:x[1])

now = 0
jobIndex = 0
for i in range(N):
    if now + jobs[i][0] > jobs[i][1]:
        print("No")
        exit()
    now += jobs[i][0]

print("Yes")
