class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
        
                if not stack:
                    break
                
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[i], height[left]) - height[mid]
                water+= bounded_height * width
            
            stack.append(i)
        return water

     

                





       