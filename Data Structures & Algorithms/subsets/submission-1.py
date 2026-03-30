class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(idx, path):
            # Base Case
            if idx >= len(nums):
                res.append(path.copy())
                return
            
            # choices
            # include nums[idx]
            path.append(nums[idx])
            dfs(idx+1, path)
            path.pop()

            # exclude nums[idx]
            dfs(idx+1, path)

        
        dfs(0, [])
        return res

        

    
