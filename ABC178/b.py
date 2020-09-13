a, b, c, d = map(int, input().split())

cand = [a * c, a * d, b * c, b * d]

print(max(cand))
