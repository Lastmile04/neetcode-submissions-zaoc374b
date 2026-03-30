class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        for i in range(n):
            width = 1
            # Expand left
            for l in range(i - 1, -1, -1):
                if heights[l] >= heights[i]:
                    width += 1
                else:
                    break
            # Expand right
            for r in range(i + 1, n):
                if heights[r] >= heights[i]:
                    width += 1
                else:
                    break
            largest = max(largest, width * heights[i])
        return largest
