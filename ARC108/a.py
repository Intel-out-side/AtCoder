def enumerateDivisors(n):
	i = 1
	table = []

	while i**2 <= n:
		if n % i == 0:
			table.append(i)
			table.append(n//i)
		i += 1

	table = list(set(table))
	return table

S, P = map(int, input().split())

div = enumerateDivisors(P)

for d in div:

    if P//d == S-d:
        print("Yes")
        exit()

print("No")
