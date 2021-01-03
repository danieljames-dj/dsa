class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        water = 0
        left = 0
        curWater = 0
        for i in range(1, n):
            if height[i] >= height[left]:
                water += curWater
                curWater = 0
                left = i
            else:
                curWater += height[left] - height[i]
        right = n-1
        for i in range(n-2, left-1, -1):
            if height[i] >= height[right]:
                right = i
            else:
                water += height[right] - height[i]
        return water