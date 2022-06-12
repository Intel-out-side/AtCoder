import bisect

from pkg_resources import safe_extra
N = int(input())
A = list(map(int, input().split()))

B = A + A

for i in range(1, 2*N):
    B[i] += B[i-1]

if B[N-1] % 10 != 0:
    print("No")
    exit()

ans = "No"
for left in range(N):
    
    Bl = B[left]

    right = bisect.bisect_left(B, Bl+B[N-1]//10)

    area = B[right] - B[left]
    
    if area == B[N-1]//10:
        ans = "Yes"

print(ans)