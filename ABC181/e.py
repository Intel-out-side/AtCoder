N, M = int(input().split())

H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
print(H[N//2+1])
