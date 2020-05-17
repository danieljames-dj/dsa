def countMergeSort(arr, start, end):
	count = 0
	mid = int((start+end)/2)
	if end - start > 1:
		count += countMergeSort(arr, start, mid) + countMergeSort(arr, mid, end)
		i = start
		j = mid
		temp = []
		while i < mid and j < end:
			if arr[i] > arr[j]:
				count += mid - i
				temp.append(arr[j])
				j += 1
			else:
				temp.append(arr[i])
				i += 1
		while i < mid:
			temp.append(arr[i])
			i += 1
		while j < end:
			temp.append(arr[j])
			j += 1
		for i in range(len(temp)):
			arr[start+i] = temp[i]
	return count

arr = [int(_) for _ in input().split()]
print(countMergeSort(arr, 0, len(arr)))