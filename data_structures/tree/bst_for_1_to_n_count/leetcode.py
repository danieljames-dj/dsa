class Solution:
    def numTrees(self, n: int) -> int:
        dp = {}
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = 0
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]