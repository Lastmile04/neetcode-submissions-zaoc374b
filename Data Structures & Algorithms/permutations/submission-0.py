class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(path):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            # include the next value
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                dfs(path)
                path.pop()
                used.remove(i)
        dfs([])
        return res
