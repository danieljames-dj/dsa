from collections import defaultdict

# abcdefg

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastOccurance = defaultdict(lambda: -1)
        startIndex = 0
        longestSubstr = 0
        n = len(s)
        for i in range(n):
            ch = s[i]
            if lastOccurance[ch] >= startIndex:
                longestSubstr = max(longestSubstr, i-startIndex)
                startIndex = lastOccurance[ch] + 1
            lastOccurance[ch] = i
        longestSubstr = max(longestSubstr, n - startIndex)
        return longestSubstr