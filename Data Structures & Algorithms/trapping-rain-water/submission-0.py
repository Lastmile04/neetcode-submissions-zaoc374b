class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0
        n = len(height)
        for i in range(1, n-1):
            maxLeft = height[i]
            for j in range(i):
                maxLeft = max(height[j], maxLeft)

            maxRight = height[i]
            for j in range(i+1, n):
                maxRight = max(height[j], maxRight)

            maxWater+= min(maxLeft, maxRight) - height[i]
        return maxWater