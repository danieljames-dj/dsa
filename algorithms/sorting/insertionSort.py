def sort(arr):
	for i in range(1, len(arr)):
		buffer = arr[i]
		j = i-1
		while j >= 0 and buffer < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = buffer

arr = [int(_) for _ in input().split()]
sort(arr)
print(arr)