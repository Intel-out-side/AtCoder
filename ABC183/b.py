Sx, Sy, Gx, Gy = map(int, input().split())

p = (Sy*Gx + Gy*Sx)/(Sy+Gy)

print(f"{p:10}")    
