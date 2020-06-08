def sort(arr, left = None, right = None):
	if left is None or right is None:
		left, right = 0, len(arr)
	if right - left > 1:
		mid = (left + right) // 2
		sort(arr, left, mid)
		sort(arr, mid, right)
		bufferArr = []
		i, j = left, mid
		while i < mid and j < right:
			if arr[j] < arr[i]:
				bufferArr.append(arr[j])
				j += 1
			else:
				bufferArr.append(arr[i])
				i += 1
		while i < mid:
			bufferArr.append(arr[i])
			i += 1
		while j < right:
			bufferArr.append(arr[j])
			j += 1
		for i in range(left, right):
			arr[i] = bufferArr.pop(0)

arr = [int(_) for _ in input().split()]
sort(arr)
print(arr)