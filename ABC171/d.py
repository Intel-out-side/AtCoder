N = int(input())
A = list(map(int, input().split()))
Q = int(input())

task = [0]*Q
for i in range(Q):
    b, c = list(map(int, input().split()))
    task[i] = (b, c)

count = [0]*(10**5+1)
for i in range(N):
    count[A[i]] += 1

ans = sum(A)

for pair in task:
    B, C = pair
    if count[B]:
        ans -= B * count[B]
        increment = count[B]
        count[C] += count[B]
        count[B] = 0
        ans += C * increment
    print(ans)
