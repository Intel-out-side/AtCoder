import sys
sys.setrecursionlimit(10**7)
N = int(input())
a = list(map(int, input().split()))

dp = [[[-1 for _ in range(310)] for _ in range(310)] for _ in range(310)]

def f(c1:int, c2:int, c3:int):

	if dp[c1][c2][c3] != -1:
		return dp[c1][c2][c3]

	ret1, ret2, ret3, ret4 = 0, 0, 0, 0
	p = c1 + c2 + c3

	if c3 > 0:
		ret1 = f(c1, c2+1, c3-1) * c3

	if c2 > 0:
		ret2 = f(c1+1, c2-1, c3) * c2

	if c1 > 0:
		ret3 = f(c1-1, c2, c3) * c1

	ret4 = N

	dp[c1][c2][c3] = ret1 + ret2 + ret3 + ret4
	dp[c1][c2][c3] /= p

	return dp[c1][c2][c3]

c1 = a.count(1)
c2 = a.count(2)
c3 = a.count(3)
dp[0][0][0] = 0

ans = f(c1, c2, c3)

print("{:.10f}".format(ans))
