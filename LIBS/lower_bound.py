def lower_bound(li:list, val:int) -> int:
    """
    二分探索で値が入る場所をreturnします
    リストはソートされてないと使えません
    """
    # li.sort()
    left = 0
    right = len(li) - 1
    mid = None

    while left < right:
        mid = (left + right) // 2
        print(left, mid, right)
        if li[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
	import sys
	sample_list = [1, 2, 3, 4, 5, 6, 7]
	val = int(sys.argv[1])
	print(lower_bound(sample_list, val))
