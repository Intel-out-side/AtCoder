x = int(input())

min_score = 400

for i in range(8):

    if 400 + 200 * i <= x < 400 + 200 * (i+1):
        print(8 - i)
