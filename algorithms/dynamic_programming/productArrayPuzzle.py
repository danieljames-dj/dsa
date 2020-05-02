arr = [int(_) for _ in input().split()]
prod = [1]
for i in range(1, len(arr)):
	prod.append(prod[i-1] * arr[i-1])
right = 1
for i in range(len(arr)-2, -1, -1):
	right *= arr[i+1]
	prod[i] *= right
print(prod)