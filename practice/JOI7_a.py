P = int(input())

change = 1000 - P

coins = 0

coins += change//500
change = change % 500

coins += change//100
change = change % 100

coins += change // 50
change = change % 50

coins += change // 10
change = change % 10

coins += change // 5
change = change % 5

coins += change // 1
change = change % 1

print(coins)
