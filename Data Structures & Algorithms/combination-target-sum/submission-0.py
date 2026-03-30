class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, total):
            # base case
            if total == target:
                res.append(path.copy()) # snap shot of the current path
                return

            # path cannot work -> stop exploring
            if total > target:
                return
            
            # keep adding new numbers to combination
            for i in range(start, len(nums)):
                # add the current number to the path
                path.append(nums[i])
                # go deep 
                backtrack(i, path, total + nums[i])
                # pop the path to backtrack
                path.pop()
        backtrack(0, [], 0)
        return res

