import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

ans = []

pi = math.pi

for _ in range(Q):
    e = int(input())
    
    s = math.sqrt(
        X**2 + (Y+L/2*math.sin(2*e/T*pi))**2
    )

    z = L/2 - L/2*math.cos(2*e/T*pi)

    theta = pi/2 - math.atan2(s, z)
    theta = theta * 360 / (2*pi)
    ans.append(theta)

for item in ans:
    print(item)