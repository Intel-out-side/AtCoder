N = int(input())

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

ans = enumerateDivisors(N)
ans.sort()
for item in ans:
    print(item)
