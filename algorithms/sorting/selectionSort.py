def sort(arr):
	n = len(arr)
	for i in range(n-1):
		minm = i
		for j in range(i+1, n):
			if arr[j] < arr[minm]:
				minm = j
		if minm != i:
			arr[minm], arr[i] = arr[i], arr[minm]

arr = [int(_) for _ in input().split()]
sort(arr)
print(arr)