def maxHeapify(arr, i):
	parent = int((i-1)/2)
	if arr[parent] < arr[i]:
		arr[parent], arr[i] = arr[i], arr[parent]
		maxHeapify(arr, parent)

def minHeapify(arr, i):
	parent = int((i-1)/2)
	if arr[parent] > arr[i]:
		arr[parent], arr[i] = arr[i], arr[parent]
		minHeapify(arr, parent)

def insertToMinHeap(arr, el):
	arr.append(el)
	minHeapify(arr, len(arr)-1)

def insertToMaxHeap(arr, el):
	arr.append(el)
	maxHeapify(arr, len(arr)-1)

def printMedians(arr, n):
	assert n > 0
	median = arr[0]
	leftHeap = []
	rightHeap = []
	print(median)
	for i in range(1, n):
		# 1. Insert the element to heap/median
		if arr[i] < median:
			if len(leftHeap) <= len(rightHeap):
				insertToMaxHeap(leftHeap, arr[i])
			else:
				insertToMinHeap(rightHeap, median)
				median = arr[i]
		else:
			if len(rightHeap) <= len(leftHeap):
				insertToMinHeap(rightHeap, arr[i])
			else:
				insertToMaxHeap(leftHeap, median)
				median = arr[i]
		# 2. Print the median
		if len(leftHeap) == len(rightHeap):
			print(median)
		elif len(leftHeap) < len(rightHeap):
			print((median+rightHeap[0])/2)
		else: # len(leftHeap) > len(rightHeap)
			print((median+leftHeap[0])/2)

arr = [int(_) for _ in input().split()]
printMedians(arr, len(arr))