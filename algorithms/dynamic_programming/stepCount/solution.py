def count(arr, n, dp):
	if dp[n] != -1:
		return dp[n]
	elif n < 0:
		return 0
	elif n == 0:
		dp[n] = 1
	else:
		sum = 0
		for i in arr:
			sum += count(arr, n-i, dp)
		dp[n] = sum
	return dp[n]

arr = [int(_) for _ in input().split()]
n = int(input())
dp = [-1]*(n+1)
print(count(arr, n, dp))