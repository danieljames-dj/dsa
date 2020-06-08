def sort(arr, left = None, right = None):
	if left is None or right is None:
		left, right = 0, len(arr)
	if right - left > 1:
		pivot = arr[right-1]
		i = left
		for j in range(left, right-1):
			if arr[j] < pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[right-1] = arr[right-1], arr[i]
		sort(arr, left, i)
		sort(arr, i+1, right)

arr = [int(_) for _ in input().split()]
sort(arr)
print(arr)