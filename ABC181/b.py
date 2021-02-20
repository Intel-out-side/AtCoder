N = int(input())

ans = 0
for i in range(N):
    A, B = map(int, input().split())

    ans += B * (B+1) // 2 - (A-1)*A//2

print(ans)
