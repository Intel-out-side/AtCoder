import sys
def lower_bound(li, val):
	left = -1
	right = len(li)-1
	mid = None

	while left < right:
		mid = (left + right) // 2

		if li[mid] < val:
			left = mid + 1
		else:
			right = mid

	return left

sample_list = [1, 3, 5, 7]
val = int(sys.argv[1])
print(lower_bound(sample_list, val))
