N = int(input())
x = list(map(int, input().split()))

m = 0
e = 0
c = -float("inf")

for item in x:
    m += abs(item)
    e += abs(item) * abs(item)

for item in x:
    c = max(c, abs(item))

e = e**0.5

print("{:.10f}".format(m))
print("{:.10f}".format(e))
print("{:.10f}".format(c))
