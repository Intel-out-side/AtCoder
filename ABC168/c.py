import math
A, B, H, M = list(map(int, input().split()))


timePassed = 60 * H + M #min

omega_a = 2*math.pi/(12*60) #rad/min
omega_b = 2*math.pi/(60) #rad/min

theta = omega_a * timePassed - omega_b*timePassed

if theta > math.pi:
    theta = 2 * math.pi - theta

c = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta))

print(f"{c:10}")
