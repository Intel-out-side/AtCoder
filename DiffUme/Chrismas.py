import sys
sys.setrecursionlimit(10**5)
N, X = map(int, input().split())

def f(burger, counter):
    if counter == 0:
        return "P"

    L = f(burger, counter - 1)
    newBurger = "B" + L + "P" + L + "B"

    return newBurger

burger = f("", N)

ans = burger[0:X].count("P")
print(ans)
