class Solution:
    def numSplits(self, s: str) -> int:
        counter = 0
        leftCount, rightCount = 0, 0
        freq = [0] * 26
        n = len(s)
        getIndex = lambda c: ord(c) - ord('a')
        for i in range(n):
            ch = getIndex(s[i])
            if freq[ch] == 0:
                rightCount += 1
            freq[ch] += 1
        for i in range(n):
            ch = getIndex(s[i])
            isNeg = freq[ch] < 0
            val = abs(freq[ch])
            if not isNeg:
                leftCount += 1
            if val == 1:
                rightCount -= 1
            freq[ch] = -1 * (val - 1)
            if leftCount == rightCount:
                counter += 1
        return counter