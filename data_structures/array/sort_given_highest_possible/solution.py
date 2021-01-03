arr = [int(_) for _ in input().split()]
freq = [0] * 101
for el in arr:
	freq[el] += 1
i = 0
for j in range(101):
	while freq[j] > 0:
		arr[i] = j
		i += 1
		freq[j] -= 1
print(arr)