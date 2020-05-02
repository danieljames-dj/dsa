def count(arr, n, sum, dict):
	key = str(n) + ':' + str(sum)
	if key in dict:
		return dict[key]
	elif sum == 0:
		return 1
	elif sum < 0:
		return 0
	elif n == len(arr):
		return 0
	else:
		dict[key] = count(arr, n+1, sum, dict) + count(arr, n+1, sum-arr[n], dict)
		return dict[key]

dict = {}
arr = [int(_) for _ in input().split()]
sum = int(input())
print(count(arr, 0, sum, dict))