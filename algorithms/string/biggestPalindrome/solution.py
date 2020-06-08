def checkLeftRight(string, left, right):
	while left >= 0 and right < len(string):
		if string[left] == string[right]:
			left -= 1
			right += 1
		else:
			break
	return right - left - 1

def longestPalindrome(string):
	start = 0
	end = 0
	for i in range(len(string)):
		oddPalin = checkLeftRight(string, i, i)
		evenPalin = checkLeftRight(string, i, i+1)
		length = max(oddPalin, evenPalin)
		if length > end - start:
			start = i - int((length-1)/2)
			end = i + int(length/2)
	return string[start:end+1]

print(longestPalindrome(input()))