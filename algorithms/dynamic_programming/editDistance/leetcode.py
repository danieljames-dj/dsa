class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n+1)] for j in range(2)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(1, m+1):
            x = i%2
            y = (i+1)%2
            dp[x][0] = i
            for j in range(1, n+1):
                dp[x][j] = min(
                    (dp[y][j-1] if word1[i-1] == word2[j-1] else dp[y][j-1]+1),
                    dp[y][j] + 1,
                    dp[x][j-1] + 1
                )
        return dp[m%2][n]