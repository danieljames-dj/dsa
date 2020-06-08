from collections import defaultdict

string = input()
k = int(input())
freq = defaultdict((lambda: 0))
bestStart, bestEnd, curStart, curEnd = 0, 0, 0, -1
for c in string:
	curEnd += 1
	freq[c] += 1
	while len(freq.keys()) > k:
		freq[string[curStart]] -= 1
		if freq[string[curStart]] == 0:
			del freq[string[curStart]]
		curStart += 1
	if curEnd - curStart > bestEnd - bestStart:
		bestStart, bestEnd = curStart, curEnd
print(string[bestStart:bestEnd+1])